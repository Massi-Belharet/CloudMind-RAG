"""
Semantic Router Threshold Calibration script for CloudMind RAG pipeline (Sprint 5).

Empirically calibrates SemanticRouter's routing threshold (currently 0.60, a
placeholder tuned against nomic-embed-text-v1.5's similarity distribution and
never re-validated against BAAI/bge-m3 — the production embedding model since
ADR 003). Measures cosine similarity scores on two groups:

    - "mono" queries: clearly about a single provider (aws, azure, gcp, or
      compliance). The score against their expected provider must exceed the
      threshold for the router to correctly restrict retrieval to it.
    - "multi" queries: clearly not specific to a single provider (multi-cloud,
      generic FinOps, hybrid architecture). The max score across all providers
      must stay below the threshold so the router correctly returns None
      (search all providers — today's default, safe behavior).

Reuses SemanticRouter as-is (embedder-only, no changes to its internal logic)
via the production bge-m3 embedding model, so calibration reflects the exact
component used at inference time.

Functions:
    get_mono_provider_queries() -> List[dict] : Return queries with a single, unambiguous expected provider.
    get_multi_provider_queries() -> List[str] : Return queries that should NOT be routed to a single provider.
    summarize(scores) -> dict : min/max/mean/median summary statistics for a score distribution.
    recommend_threshold(mono_scores, multi_max_scores) -> Tuple[float, str] : Recommend a calibrated threshold with rationale.
    run_calibration() -> None : Score all examples, print distributions and save results.
"""

import json
import statistics
from pathlib import Path
from typing import List, Tuple

import torch  # noqa: F401 — import before pandas/pyarrow to avoid a native OpenMP/MKL load-order crash on Windows

from src.embeddings.embedder import Embedder
from src.rag.semantic_router import SemanticRouter
from src.utils.config import config

# Verification queries from the CRAG provider-filtering task, included explicitly
# so calibration guarantees they classify correctly.
VERIFICATION_MONO_QUERY = "What are the AWS Well-Architected Framework cost optimization pillars?"
VERIFICATION_MULTI_QUERY = "How to optimize Kubernetes workloads for cost efficiency in a multi-cloud setup?"


def get_mono_provider_queries() -> List[dict]:
    """
    Return queries that are clearly about a single, unambiguous cloud provider.

    Returns:
        List[dict]: Entries with 'query' and the 'provider' it should route to.
    """
    return [
        {"query": VERIFICATION_MONO_QUERY, "provider": "aws"},
        {"query": "How do I set up IAM roles for AWS Lambda functions?", "provider": "aws"},
        {"query": "What is the Amazon S3 storage class for infrequent access?", "provider": "aws"},
        {"query": "How to configure AWS CloudTrail for audit logging?", "provider": "aws"},
        {"query": "How to reduce Azure cloud spending using reserved instances?", "provider": "azure"},
        {"query": "What is Azure Blob Storage used for?", "provider": "azure"},
        {"query": "How do I configure Azure Active Directory conditional access?", "provider": "azure"},
        {"query": "What are Azure Virtual Machine scale sets?", "provider": "azure"},
        {"query": "How to optimize BigQuery costs in Google Cloud?", "provider": "gcp"},
        {"query": "What is Google Kubernetes Engine Autopilot mode?", "provider": "gcp"},
        {"query": "How do I configure Cloud Run for GCP serverless deployments?", "provider": "gcp"},
        {"query": "What are the GCP Cost Optimization pillar best practices?", "provider": "gcp"},
        {"query": "How to implement data residency compliance under RGPD for cloud workloads?", "provider": "compliance"},
        {"query": "How does the EU Cloud Code of Conduct define security obligations?", "provider": "compliance"},
        {"query": "What is required for a Data Processing Agreement under GDPR?", "provider": "compliance"},
        {"query": "What are the requirements for data residency in the EU under GDPR?", "provider": "compliance"},
    ]


def get_multi_provider_queries() -> List[str]:
    """
    Return queries that are clearly not specific to a single cloud provider —
    the router must return None for these, leaving retrieval unfiltered.

    Returns:
        List[str]: Multi-cloud, generic FinOps, or provider-agnostic queries.
    """
    return [
        VERIFICATION_MULTI_QUERY,
        "What is the difference between hybrid cloud and multi-cloud architecture?",
        "How to architect an Edge computing solution with low latency requirements?",
        "What are the FinOps principles for managing cloud budget anomalies?",
        "How to compare cost optimization strategies across AWS, Azure and GCP?",
        "What is a good cloud governance framework for enterprises?",
    ]


def summarize(scores: List[float]) -> dict:
    """
    Compute summary statistics for a group of routing scores.

    Args:
        scores (List[float]): Cosine similarity scores for a group of queries.

    Returns:
        dict: min, max, mean and median of the scores.
    """
    return {
        "min": round(min(scores), 4),
        "max": round(max(scores), 4),
        "mean": round(statistics.mean(scores), 4),
        "median": round(statistics.median(scores), 4),
    }


def recommend_threshold(mono_scores: List[float], multi_max_scores: List[float]) -> Tuple[float, str]:
    """
    Recommend a routing threshold that separates mono-provider and multi-provider
    score distributions with a safety margin.

    Prioritizes avoiding false routing (restricting retrieval for a question that
    is actually multi-provider) over missing a routing opportunity — staying
    unfiltered (None) is today's default, safe behavior, while wrongly filtering
    to one provider can hide relevant chunks from other providers. When
    distributions overlap, the threshold is biased upward (toward the top of the
    overlap) to favor this safer trade-off.

    Args:
        mono_scores (List[float]): Score of the expected provider for each mono-provider query.
        multi_max_scores (List[float]): Max score across all providers for each multi-provider query.

    Returns:
        Tuple[float, str]: The recommended threshold and a rationale explaining how it was derived.
    """
    min_mono = min(mono_scores)
    max_multi = max(multi_max_scores)

    if max_multi < min_mono:
        threshold = round((max_multi + min_mono) / 2, 4)
        rationale = (
            f"Clean separation: all multi-provider queries ({max_multi:.4f} max) score below "
            f"all mono-provider queries ({min_mono:.4f} min). Threshold placed at the midpoint "
            f"of that gap for maximum margin."
        )
    else:
        all_scores = mono_scores + multi_max_scores
        margin = max(0.05 * (max(all_scores) - min(all_scores)), 0.005)
        threshold = round(max_multi + margin, 4)
        rationale = (
            f"Score distributions overlap (max multi-provider {max_multi:.4f} >= min mono-provider "
            f"{min_mono:.4f}) — no threshold cleanly separates both groups. Threshold biased upward, "
            f"just above the highest multi-provider score ({max_multi:.4f} + {margin:.4f} margin), "
            f"since failing to route (safe default: search all providers) is preferable to wrongly "
            f"routing a multi-provider question to a single one. Check the misclassified examples "
            f"below before finalizing."
        )

    return threshold, rationale


def run_calibration() -> None:
    """
    Score mono-provider and multi-provider queries with the production bge-m3
    embedder, print distribution summaries, recommend a calibrated routing
    threshold and save detailed per-query results to backend/results/benchmarks/.
    """
    print("CloudMind — Semantic Router Threshold Calibration")

    embedder = Embedder(model_name=config.embedding.model, use_fp16=True)
    router = SemanticRouter(embedder=embedder)

    mono_queries = get_mono_provider_queries()
    multi_queries = get_multi_provider_queries()

    print(f"\nMono-provider queries  : {len(mono_queries)}")
    print(f"Multi-provider queries : {len(multi_queries)}")

    results = []

    print("\nScoring mono-provider queries (score = similarity to expected provider)...")
    mono_scores = []
    for entry in mono_queries:
        query_vector = embedder.embed_query(entry["query"])
        all_scores = {
            provider: router._cosine_similarity(query_vector, route_vector)
            for provider, route_vector in router.route_embeddings.items()
        }
        expected_score = all_scores[entry["provider"]]
        mono_scores.append(expected_score)
        results.append({
            "query": entry["query"],
            "category": "mono",
            "expected_provider": entry["provider"],
            "expected_provider_score": round(expected_score, 4),
            "all_scores": {p: round(s, 4) for p, s in all_scores.items()},
        })
        print(f"  {expected_score:.4f}  [{entry['provider']}]  {entry['query']}")

    print("\nScoring multi-provider queries (score = max similarity across all providers)...")
    multi_max_scores = []
    for query in multi_queries:
        query_vector = embedder.embed_query(query)
        all_scores = {
            provider: router._cosine_similarity(query_vector, route_vector)
            for provider, route_vector in router.route_embeddings.items()
        }
        max_score = max(all_scores.values())
        multi_max_scores.append(max_score)
        results.append({
            "query": query,
            "category": "multi",
            "max_score": round(max_score, 4),
            "all_scores": {p: round(s, 4) for p, s in all_scores.items()},
        })
        print(f"  {max_score:.4f}  {query}")

    mono_stats = summarize(mono_scores)
    multi_stats = summarize(multi_max_scores)

    print("\nSCORE DISTRIBUTIONS")
    print(f"{'':<10} {'min':<10} {'max':<10} {'mean':<10} {'median':<10}")
    print(
        f"{'Mono':<10} {mono_stats['min']:<10} {mono_stats['max']:<10} "
        f"{mono_stats['mean']:<10} {mono_stats['median']:<10}"
    )
    print(
        f"{'Multi':<10} {multi_stats['min']:<10} {multi_stats['max']:<10} "
        f"{multi_stats['mean']:<10} {multi_stats['median']:<10}"
    )

    threshold, rationale = recommend_threshold(mono_scores, multi_max_scores)

    print(f"\nRecommended threshold: {threshold}")
    print(rationale)

    # Flag any misclassification at the recommended threshold for transparency
    misrouted_multi = [q for q, s in zip(multi_queries, multi_max_scores) if s >= threshold]
    unrouted_mono = [
        e["query"] for e, s in zip(mono_queries, mono_scores) if s < threshold
    ]

    if misrouted_multi:
        print(f"\nWARNING: {len(misrouted_multi)} multi-provider quer(y/ies) would be WRONGLY routed at this threshold:")
        for q in misrouted_multi:
            print(f"  - {q}")
    if unrouted_mono:
        print(f"\nNote: {len(unrouted_mono)} mono-provider quer(y/ies) would stay unfiltered (safe fallback) at this threshold:")
        for q in unrouted_mono:
            print(f"  - {q}")
    if not misrouted_multi and not unrouted_mono:
        print("\nAll mono-provider queries route correctly, all multi-provider queries stay unfiltered.")

    # Save detailed results
    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    output = {
        "mono_stats": mono_stats,
        "multi_stats": multi_stats,
        "recommended_threshold": threshold,
        "rationale": rationale,
        "results": results,
    }

    output_path = results_path / "router_threshold_calibration.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    run_calibration()
