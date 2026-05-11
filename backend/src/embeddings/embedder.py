"""
HuggingFace Embedder module

Implements BaseEmbedder using sentence-transformers to load and run embedding models.

Functions:
    embed(documents: List[Document]) -> np.ndarray : Embed a list of documents into vectors.
    embed_query(query: str) -> np.ndarray : Embed a single query string into a vector.
"""

from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
import torch

from src.loaders.base_loader import Document
from src.embeddings.base_embeddings import BaseEmbedder


class Embedder(BaseEmbedder):

    def __init__(self, model_name: str = "BAAI/bge-m3"):
        """
        Load a sentence-transformers model.

        Args:
            model_name (str): Model name to load. 
        """
        super().__init__(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=self.device)
        print(f"Embedder using: {self.device}")

    def embed(self, documents: List[Document]) -> np.ndarray:
        """
        Embed a list of documents into vectors.

        Args:
            documents (List[Document]): List of documents to embed.

        Returns:
            np.ndarray: Matrix of shape (n_documents, embedding_dim).
        """
        texts = [doc.content for doc in documents]
        return self.model.encode(texts, show_progress_bar=True)

    def embed_query(self, query: str) -> np.ndarray:
        """
        Embed a query string into a vector.

        Args:
            query (str): Query string to embed.

        Returns:
            np.ndarray: Vector of shape (embedding_dim,).
        """
        return self.model.encode([query])[0]