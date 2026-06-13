"""
Reranker module 

Re-scores retrieved documents using a cross-encoder model to improve
ranking quality. Cross-encoders evaluate query-document pairs jointly,
producing more accurate relevance scores than embedding similarity alone.

Functions:
    rerank(query: str, documents: List[Document], top_k: int) -> List[Document] : Re-rank documents by relevance to the query.
"""

from typing import List
from sentence_transformers import CrossEncoder

from src.loaders.base_loader import Document
from src.utils.config import config


class Reranker:

    def __init__(self, model_name: str = None):
        """
        Load a cross-encoder reranking model.

        Args:
            model_name (str): HuggingFace cross-encoder model name. Defaults to config value.
        """
        self.model_name = model_name or config.reranker.model
        self.model = CrossEncoder(self.model_name)

    def rerank(self, query: str, documents: List[Document], top_k: int = None) -> List[Document]:
        """
        Re-rank documents by relevance to the query using a cross-encoder.

        Args:
            query (str): User question to rank documents against.
            documents (List[Document]): Documents to re-rank.
            top_k (int): Number of top documents to return. Defaults to config value.

        Returns:
            List[Document]: Top-k documents sorted by reranker score, with score added to metadata.
        """
        if top_k is None:
            top_k = config.reranker.top_k

        if not documents:
            return []

        pairs = [[query, doc.content] for doc in documents]
        scores = self.model.predict(pairs)

        scored_docs = list(zip(documents, scores))
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        results = []
        for doc, score in scored_docs[:top_k]:
            results.append(Document(
                content=doc.content,
                metadata={**doc.metadata, "rerank_score": float(score)}
            ))

        return results