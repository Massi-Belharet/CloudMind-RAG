"""
Base Embedder module 

Defines the abstract interface that all embedding implementations must follow.
This ensures a consistent API across different embedding models, making it
easy to swap models during benchmarking in Sprint 4.

Functions:
    embed(documents: List[Document]) -> np.ndarray : Embed a list of documents into vectors.
    embed_query(query: str) -> np.ndarray : Embed a single query string into a vector.
"""

from abc import ABC, abstractmethod
from typing import List
import numpy as np

from src.loaders.base_loader import Document


class BaseEmbedder(ABC):

    def __init__(self, model_name: str):
        """
        Initialize the embedder with a model.

        Args:
            model_name (str): Name of the embedding model to load.
        """
        self.model_name = model_name

    @abstractmethod
    def embed(self, documents: List[Document]) -> np.ndarray:
        """
        Embed a list of documents into vectors.

        Args:
            documents (List[Document]): List of documents to embed.

        Returns:
            np.ndarray: Matrix of shape (n_documents, embedding_dim).
        """
        pass

    @abstractmethod
    def embed_query(self, query: str) -> np.ndarray:
        """
        Embed a single query string into a vector.

        Args:
            query (str): Query string to embed.

        Returns:
            np.ndarray: Vector of shape (embedding_dim,).
        """
        pass