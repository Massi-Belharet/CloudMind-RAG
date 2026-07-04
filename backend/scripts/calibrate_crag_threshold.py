"""
CRAG Relevance Threshold Calibration script for CloudMind RAG pipeline (Sprint 5).

Empirically calibrates config.rag.relevance_threshold — the CRAG relevance
gate in Pipeline._is_relevant() — by measuring the production reranker's mean
score distribution on known-relevant queries (ground_truth.json) versus
known-unrelated queries, including the "What is Python?" trap case that
revealed the placeholder threshold (0.0) was too permissive.

Reuses the production retrieval stack built by src.api.dependencies.get_pipeline()
rather than reconstructing it, so calibration reflects the exact components
(bge-m3, Qdrant cloudmind_prod, HybridRetriever, MultiQueryRetriever,
bge-reranker-v2-m3) used at inference time.

Functions:
    load_positive_queries() -> List[str] : Load known-relevant queries from ground_truth.json.
    get_negative_queries() -> List[str] : Return a fixed set of clearly off-topic queries.
    score_query(pipeline, query, k) -> float : Mean reranker score for a query, mirroring Pipeline._is_relevant().
    summarize(scores) -> dict : min/max/mean/median summary statistics for a score distribution.
    recommend_threshold(positive_scores, negative_scores, python_score) -> Tuple[float, str] : Recommend a calibrated threshold with rationale.
    run_calibration() -> None : Score all examples, print distributions and save results.
"""

import json
import statistics
from pathlib import Path
from typing import List, Tuple

import numpy as np
import torch  # noqa: F401 — import before pandas/pyarrow to avoid a native OpenMP/MKL load-order crash on Windows

from src.api.dependencies import get_pipeline
from src.utils.config import config

TRAP_QUERY = "What is Python?"

NEGATIVE_QUERIES = [
    TRAP_QUERY,
    "What is the price of a Tesla Model S?",
    "What's the weather like today?",
    "Who won the last football World Cup?",
    "How do I bake a chocolate cake?",
    "How many bones are in the human body?",
    "What year did World War II end?",
    "How do I train for a marathon?",
    "What's the capital of Japan?",
    "Who wrote Romeo and Juliet?",
]


def load_positive_queries() -> List[str]:
    """
    Load known-relevant queries from the manually annotated ground truth file.

    Returns:
        List[str]: Queries already validated as in-scope for the cloud/FinOps corpus.

    Raises:
        FileNotFoundError: If the ground truth file does not exist.
    """
    path = Path(config.benchmark.ground_truth_path)
    if not path.exists():
        raise FileNotFoundError(f"Ground truth file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        ground_truth = json.load(f)

    return [entry["query"] for entry in ground_truth]


def get_negative_queries() -> List[str]:
    """
    Return a fixed set of clearly off-topic queries, unrelated to cloud/FinOps.

    Includes "What is Python?" — the trap case that revealed the uncalibrated
    threshold (0.0) was too permissive, due to superficial lexical overlap with
    AWS/GCP docs that mention Python as an SDK language.

    Returns:
        List[str]: Off-topic queries.
    """
    return NEGATIVE_QUERIES


def score_query(pipeline, query: str, k: int) -> float:
    """
    Compute the mean reranker score for a query, mirroring the exact scoring
    logic used by Pipeline._is_relevant() (same retrieve_k formula, same
    top_k, same mean of rerank_score) without applying a threshold.

    Args:
        pipeline (Pipeline): The production RAG pipeline (retriever + reranker).
        query (str): The query to score.
        k (int): Number of chunks to retrieve/rerank, matching production top_k.

    Returns:
        float: Mean reranker score across the top-k reranked chunks (0.0 if none retrieved).
    """
    retrieve_k = k * 2 if pipeline.reranker else k
    documents = pipeline.retriever.retrieve(query, k=retrieve_k)

    if not documents:
        return 0.0

    reranked = pipeline.reranker.rerank(query, documents, top_k=k)
    scores = [doc.metadata.get("rerank_score", 0.0) for doc in reranked]

    return float(np.mean(scores)) if scores else 0.0


def summarize(scores: List[float]) -> dict:
    """
    Compute summary statistics for a group of reranker scores.

    Args:
        scores (List[float]): Mean reranker scores for a group of queries.

    Returns:
        dict: min, max, mean and median of the scores.
    """
    return {
        "min": round(min(scores), 4),
        "max": round(max(scores), 4),
        "mean": round(statistics.mean(scores), 4),
        "median": round(statistics.median(scores), 4),
    }


def recommend_threshold(
    positive_scores: List[float], negative_scores: List[float], python_score: float
) -> Tuple[float, str]:
    """
    Recommend a CRAG relevance threshold that separates positive and negative
    score distributions with a safety margin, prioritizing two constraints in
    order: (1) the "What is Python?" trap case must fall below the threshold,
    (2) as few true-positive queries as possible should be rejected.

    Args:
        positive_scores (List[float]): Mean reranker scores for known-relevant queries.
        negative_scores (List[float]): Mean reranker scores for known-unrelated queries.
        python_score (float): Mean reranker score for the "What is Python?" trap case.

    Returns:
        Tuple[float, str]: The recommended threshold and a rationale explaining how it was derived.
    """
    min_positive = min(positive_scores)
    max_negative = max(negative_scores)

    if max_negative < min_positive:
        threshold = round((max_negative + min_positive) / 2, 4)
        rationale = (
            f"Clean separation: all negatives ({max_negative:.4f} max) score below "
            f"all positives ({min_positive:.4f} min). Threshold placed at the midpoint "
            f"of that gap for maximum margin."
        )
    else:
        all_scores = positive_scores + negative_scores
        margin = max(0.05 * (max(all_scores) - min(all_scores)), 0.01)
        threshold = round(python_score + margin, 4)
        rationale = (
            f"Score distributions overlap (max negative {max_negative:.4f} >= min positive "
            f"{min_positive:.4f}) — no threshold cleanly separates both groups. Threshold set "
            f"just above the 'What is Python?' trap case ({python_score:.4f} + {margin:.4f} margin) "
            f"to guarantee it is rejected, per the calibration priority. Check the misclassified "
            f"examples below before finalizing."
        )

    return threshold, rationale


def run_calibration() -> None:
    """
    Score positive and negative queries with the production retrieval stack,
    print distribution summaries, recommend a calibrated threshold and save
    detailed per-query results to backend/results/benchmarks/.
    """
    print("CloudMind — CRAG Relevance Threshold Calibration")

    pipeline = get_pipeline()
    k = config.rag.top_k

    positive_queries = load_positive_queries()
    negative_queries = get_negative_queries()

    print(f"\nPositive (in-scope) queries  : {len(positive_queries)}")
    print(f"Negative (off-topic) queries : {len(negative_queries)}")
    print(f"Top-K                        : {k}")

    results = []

    print("\nScoring positive queries...")
    positive_scores = []
    for query in positive_queries:
        score = score_query(pipeline, query, k)
        positive_scores.append(score)
        results.append({"query": query, "score": score, "category": "positive"})
        print(f"  {score:.4f}  {query}")

    print("\nScoring negative queries...")
    negative_scores = []
    python_score = None
    for query in negative_queries:
        score = score_query(pipeline, query, k)
        negative_scores.append(score)
        results.append({"query": query, "score": score, "category": "negative"})
        print(f"  {score:.4f}  {query}")
        if query == TRAP_QUERY:
            python_score = score

    positive_stats = summarize(positive_scores)
    negative_stats = summarize(negative_scores)

    print("\nSCORE DISTRIBUTIONS")
    print(f"{'':<10} {'min':<10} {'max':<10} {'mean':<10} {'median':<10}")
    print(
        f"{'Positive':<10} {positive_stats['min']:<10} {positive_stats['max']:<10} "
        f"{positive_stats['mean']:<10} {positive_stats['median']:<10}"
    )
    print(
        f"{'Negative':<10} {negative_stats['min']:<10} {negative_stats['max']:<10} "
        f"{negative_stats['mean']:<10} {negative_stats['median']:<10}"
    )

    threshold, rationale = recommend_threshold(positive_scores, negative_scores, python_score)

    print(f"\nRecommended threshold: {threshold}")
    print(rationale)

    # Flag any misclassification at the recommended threshold for transparency
    rejected_positives = [q for q, s in zip(positive_queries, positive_scores) if s < threshold]
    accepted_negatives = [q for q, s in zip(negative_queries, negative_scores) if s >= threshold]

    if rejected_positives:
        print(f"\nWARNING: {len(rejected_positives)} in-scope quer(y/ies) would be rejected at this threshold:")
        for q in rejected_positives:
            print(f"  - {q}")
    if accepted_negatives:
        print(f"\nWARNING: {len(accepted_negatives)} off-topic quer(y/ies) would still be accepted at this threshold:")
        for q in accepted_negatives:
            print(f"  - {q}")
    if not rejected_positives and not accepted_negatives:
        print("\nAll positives accepted, all negatives rejected at this threshold.")

    # Save detailed results
    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    output = {
        "top_k": k,
        "positive_stats": positive_stats,
        "negative_stats": negative_stats,
        "recommended_threshold": threshold,
        "rationale": rationale,
        "results": results,
    }

    output_path = results_path / "crag_threshold_calibration.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    run_calibration()
