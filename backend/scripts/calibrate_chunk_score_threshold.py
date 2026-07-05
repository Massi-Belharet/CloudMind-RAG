"""
Per-Chunk Rerank Score Threshold Calibration script for CloudMind RAG pipeline (Sprint 5).

Empirically calibrates config.rag.min_chunk_score — the per-chunk filter applied
in Pipeline._filter_by_min_chunk_score() after reranking. Unlike CRAG's
relevance_threshold (calibrate_crag_threshold.py), which gates on the MEAN
rerank score across the whole retrieved set, this threshold drops individually
weak chunks even when the query as a whole passes CRAG — e.g. a low-signal
"related links" boilerplate chunk sitting in the top-k of an otherwise
well-answered query.

Reuses the production retrieval stack built by src.api.dependencies.get_pipeline()
so calibration reflects the exact components used at inference time. Includes
"What are Azure cost optimization best practices?" — the query that surfaced a
"related links" boilerplate chunk ranking inside the top-k despite the query as
a whole being clearly in-scope.

Functions:
    load_test_queries() -> List[str] : Return the fixed set of test queries.
    is_noise_chunk(content: str) -> bool : Heuristically flag likely boilerplate chunks.
    score_query_chunks(pipeline, query, k) -> List[dict] : Individual rerank scores per chunk for a query.
    recommend_threshold(noise_scores, content_scores) -> Tuple[float, str] : Recommend a calibrated threshold with rationale.
    run_calibration() -> None : Score all test queries, print per-chunk scores and save results.
"""

import json
from pathlib import Path
from typing import List, Tuple

import torch  # noqa: F401 — import before pandas/pyarrow to avoid a native OpenMP/MKL load-order crash on Windows

from src.api.dependencies import get_pipeline
from src.utils.config import config
from scripts.calibrate_crag_threshold import load_positive_queries

TRIGGER_QUERY = "What are Azure cost optimization best practices?"

# Markers confirmed (via direct PDF inspection) to be specific to the Microsoft
# Learn "related links" footer noise that Axe 1 cleans out of the corpus. Used
# here only to auto-flag likely-noise chunks in the calibration report — not
# part of the production filter itself, which relies solely on rerank_score.
NOISE_MARKERS = [
    "Refer to the complete set of recommendations",
    "Related links",
    "Community links",
]


def load_test_queries() -> List[str]:
    """
    Return the fixed set of test queries used for chunk-level calibration:
    the trigger query that revealed the problem plus a small sample of known
    in-scope queries from ground_truth.json for a broader score distribution.

    Returns:
        List[str]: Test queries, trigger query first.
    """
    sample = load_positive_queries()[:5]
    queries = [TRIGGER_QUERY] + [q for q in sample if q != TRIGGER_QUERY]
    return queries


def is_noise_chunk(content: str) -> bool:
    """
    Heuristically flag a chunk as likely "related links" boilerplate.

    Args:
        content (str): Chunk text content.

    Returns:
        bool: True if the chunk contains a known Microsoft Learn noise marker.
    """
    return any(marker in content for marker in NOISE_MARKERS)


def score_query_chunks(pipeline, query: str, k: int) -> List[dict]:
    """
    Retrieve and rerank chunks for a query, returning each chunk's individual
    rerank_score (not the mean), mirroring the exact retrieve/rerank steps
    Pipeline.ask() runs before CRAG and the min_chunk_score filter.

    Args:
        pipeline (Pipeline): The production RAG pipeline (retriever + reranker).
        query (str): The query to score.
        k (int): Number of chunks to retrieve/rerank, matching production top_k.

    Returns:
        List[dict]: One entry per reranked chunk with its score, content
        preview, source file, and whether it looks like noise.
    """
    retrieve_k = k * 2 if pipeline.reranker else k
    documents = pipeline.retriever.retrieve(query, k=retrieve_k)

    if not documents:
        return []

    reranked = pipeline.reranker.rerank(query, documents, top_k=k)

    return [
        {
            "score": float(doc.metadata.get("rerank_score", 0.0)),
            "source": doc.metadata.get("file_name", doc.metadata.get("source", "unknown")),
            "preview": doc.content[:150].replace("\n", " "),
            "looks_like_noise": is_noise_chunk(doc.content),
        }
        for doc in reranked
    ]


def recommend_threshold(noise_scores: List[float], content_scores: List[float]) -> Tuple[float, str]:
    """
    Recommend a min_chunk_score threshold that separates noise-flagged chunks
    from substantial-content chunks with a safety margin.

    Args:
        noise_scores (List[float]): rerank_score of chunks flagged as likely noise.
        content_scores (List[float]): rerank_score of all other (substantial) chunks.

    Returns:
        Tuple[float, str]: The recommended threshold and a rationale.
    """
    if not noise_scores:
        return 0.0, (
            "No noise-flagged chunks appeared in the top-k for these test queries "
            "(the corpus may already be clean, or the trigger query no longer "
            "surfaces the boilerplate chunk). Defaulting to 0.0 (no-op filter) — "
            "re-run calibration against a corpus/query combo that still reproduces "
            "the issue before raising this threshold."
        )

    max_noise = max(noise_scores)
    min_content = min(content_scores) if content_scores else max_noise

    if max_noise < min_content:
        threshold = round((max_noise + min_content) / 2, 4)
        rationale = (
            f"Clean separation: all noise-flagged chunks ({max_noise:.4f} max) score "
            f"below all substantial-content chunks ({min_content:.4f} min). Threshold "
            f"placed at the midpoint of that gap for maximum margin."
        )
    else:
        all_scores = noise_scores + content_scores
        margin = max(0.05 * (max(all_scores) - min(all_scores)), 0.001)
        threshold = round(max_noise + margin, 4)
        rationale = (
            f"Score distributions overlap (max noise {max_noise:.4f} >= min content "
            f"{min_content:.4f}) — no threshold cleanly separates both groups. "
            f"Threshold set just above the highest noise-flagged score "
            f"({max_noise:.4f} + {margin:.4f} margin). Check the flagged chunks below "
            f"before finalizing."
        )

    return threshold, rationale


def run_calibration() -> None:
    """
    Score test queries with the production retrieval stack, print individual
    per-chunk rerank scores, recommend a calibrated min_chunk_score threshold
    and save detailed results to backend/results/benchmarks/.
    """
    print("CloudMind — Per-Chunk Rerank Score Threshold Calibration")

    pipeline = get_pipeline()
    k = config.rag.top_k

    queries = load_test_queries()
    print(f"\nTest queries: {len(queries)}")
    print(f"Top-K       : {k}")

    all_results = []
    noise_scores = []
    content_scores = []

    for query in queries:
        print(f"\nQuery: {query}")
        chunks = score_query_chunks(pipeline, query, k)
        for rank, chunk in enumerate(chunks, start=1):
            flag = "NOISE?" if chunk["looks_like_noise"] else "      "
            print(f"  [{rank}] {chunk['score']:.4f} {flag}  {chunk['source']}  | {chunk['preview']}")
            if chunk["looks_like_noise"]:
                noise_scores.append(chunk["score"])
            else:
                content_scores.append(chunk["score"])
        all_results.append({"query": query, "chunks": chunks})

    print("\nSCORE SUMMARY")
    print(f"Noise-flagged chunks   : {len(noise_scores)}")
    print(f"Substantial-content chunks : {len(content_scores)}")

    threshold, rationale = recommend_threshold(noise_scores, content_scores)

    print(f"\nRecommended min_chunk_score: {threshold}")
    print(rationale)

    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    output = {
        "top_k": k,
        "noise_scores": noise_scores,
        "content_scores": content_scores,
        "recommended_threshold": threshold,
        "rationale": rationale,
        "results": all_results,
    }

    output_path = results_path / "chunk_score_threshold_calibration.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    run_calibration()
