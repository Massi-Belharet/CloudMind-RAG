"""
Fusion module 

We use Reciprocal Rank Fusion (RRF) to combine multiple ranked
document lists into a single ranked list. Used by HybridRetriever
to merge BM25 and dense search results, and by MultiQueryRetriever
to merge results from multiple query reformulations.

Functions:
    rrf_fusion(ranked_lists: List[List[Document]], weights: List[float], k: int, rrf_k: int) -> List[Document] : Combine multiple ranked lists using RRF.
"""

from typing import List, Optional

from src.loaders.base_loader import Document


def rrf_fusion(ranked_lists: List[List[Document]], weights: Optional[List[float]] = None, k: int = 5, rrf_k: int = 60) -> List[Document]:
    """
    Combine multiple ranked document lists using Reciprocal Rank Fusion.

    Documents are deduplicated by content. Each document's score is the
    weighted sum of 1/(rank + rrf_k) across all the lists it appears in.

    Args:
        ranked_lists (List[List[Document]]): Ranked lists of documents to fuse.
        weights (Optional[List[float]]): Weight for each list. Defaults to equal weights.
        k (int): Number of final results to return. Defaults to 5.
        rrf_k (int): RRF smoothing constant. Defaults to 60 (standard convention).

    Returns:
        List[Document]: Top-k documents sorted by fused RRF score.
    """
    if weights is None:
        weights = [1.0] * len(ranked_lists)

    scores = {}

    for ranked_list, weight in zip(ranked_lists, weights):
        for rank, doc in enumerate(ranked_list):
            key = doc.content
            if key not in scores:
                scores[key] = {"doc": doc, "score": 0.0}
            scores[key]["score"] += weight * (1 / (rank + rrf_k))

    sorted_docs = sorted(scores.values(), key=lambda x: x["score"], reverse=True)[:k]

    return [item["doc"] for item in sorted_docs]