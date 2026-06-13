"""
Hybrid Retriever module 

Combines BM25 lexical search with dense semantic search using
Reciprocal Rank Fusion (RRF) to improve retrieval quality.
BM25 captures exact keyword matches while dense search captures
semantic similarity, together they cover both precise and fuzzy queries.

Functions:
    retrieve(query: str, k: int) -> List[Document] : Retrieve top-k documents using hybrid search.
"""

from typing import List
from rank_bm25 import BM25Okapi

from src.loaders.base_loader import Document
from src.rag.retriever import Retriever


class HybridRetriever:

    def __init__(
        self,
        retriever: Retriever,
        documents: List[Document],
        bm25_weight: float = 0.5,
        dense_weight: float = 0.5,
        rrf_k: int = 60
    ):
        """
        Initialize HybridRetriever with a dense retriever and BM25 index.

        Args:
            retriever (Retriever): Dense retriever instance for semantic search.
            documents (List[Document]): Documents to build BM25 index from.
            bm25_weight (float): Weight for BM25 results in RRF fusion. Defaults to 0.5.
            dense_weight (float): Weight for dense results in RRF fusion. Defaults to 0.5.
            rrf_k (int): RRF smoothing constant. Defaults to 60 (standard convention).
        """
        self.retriever = retriever
        self.documents = documents
        self.bm25_weight = bm25_weight
        self.dense_weight = dense_weight
        self.rrf_k = rrf_k

        # Build BM25 index from document contents
        tokenized_corpus = [doc.content.lower().split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized_corpus)

    def _bm25_search(self, query: str, k: int) -> List[Document]:
        """
        Perform BM25 lexical search.

        Args:
            query (str): Query string.
            k (int): Number of results to return.

        Returns:
            List[Document]: Top-k documents by BM25 score.
        """
        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)

        # Get top-k indices sorted by score
        top_k_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:k]

        return [self.documents[i] for i in top_k_indices]

    def _rrf_fusion(
        self,
        bm25_results: List[Document],
        dense_results: List[Document],
        k: int
    ) -> List[Document]:
        """
        Combine BM25 and dense results using Reciprocal Rank Fusion.

        Args:
            bm25_results (List[Document]): Results from BM25 search.
            dense_results (List[Document]): Results from dense search.
            k (int): Number of final results to return.

        Returns:
            List[Document]: Top-k documents after RRF fusion.
        """
        scores = {}

        # BM25 scores
        for rank, doc in enumerate(bm25_results):
            key = doc.content
            if key not in scores:
                scores[key] = {"doc": doc, "score": 0.0}
            scores[key]["score"] += self.bm25_weight * (1 / (rank + self.rrf_k))

        # Dense scores
        for rank, doc in enumerate(dense_results):
            key = doc.content
            if key not in scores:
                scores[key] = {"doc": doc, "score": 0.0}
            scores[key]["score"] += self.dense_weight * (1 / (rank + self.rrf_k))

        # Sort by RRF score and return top-k
        sorted_docs = sorted(
            scores.values(),
            key=lambda x: x["score"],
            reverse=True
        )[:k]

        return [item["doc"] for item in sorted_docs]

    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """
        Retrieve top-k documents using hybrid BM25 + dense search with RRF fusion.

        Args:
            query (str): User question to search for.
            k (int): Number of documents to retrieve. Defaults to 5.

        Returns:
            List[Document]: Top-k most relevant documents after RRF fusion.
        """
        # Retrieve 2*k candidates from each method before fusion
        bm25_results = self._bm25_search(query, k=k * 2)
        dense_results = self.retriever.retrieve(query, k=k * 2)

        return self._rrf_fusion(bm25_results, dense_results, k=k)