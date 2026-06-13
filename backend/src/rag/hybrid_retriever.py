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
from src.rag.fusion import rrf_fusion


class HybridRetriever:

    def __init__(self, retriever: Retriever, documents: List[Document], bm25_weight: float = 0.5, dense_weight: float = 0.5, rrf_k: int = 60):
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

        return rrf_fusion(
            ranked_lists=[bm25_results, dense_results],
            weights=[self.bm25_weight, self.dense_weight],
            k=k,
            rrf_k=self.rrf_k
        )