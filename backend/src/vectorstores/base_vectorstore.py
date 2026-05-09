"""
Base VectorStore module 

Defines the abstract interface that all vector store implementations
must follow. This ensures a consistent API across Qdrant, Pgvector,
and FAISS, making it easy to swap stores during benchmarking.

Functions:
    add(documents: List[Document], vectors: np.ndarray) -> None : Add documents and their vectors to the store.
    search(query_vector: np.ndarray, k: int) -> List[Document] : Search for the k most similar documents.
    save(path: str) -> None : Persist the vector store to disk.
    load(path: str) -> None : Load the vector store from disk.
"""

from abc import ABC, abstractmethod
from typing import List
import numpy as np

from src.loaders.base_loader import Document


class BaseVectorStore(ABC):

    def __init__(self, collection_name: str):
        """
        Initialize the vector store with a collection name.

        Args:
            collection_name (str): Name of the collection to store vectors in.
        """
        self.collection_name = collection_name

    @abstractmethod
    def add(self, documents: List[Document], vectors: np.ndarray) -> None:
        """
        Add documents and their vectors to the store.

        Args:
            documents (List[Document]): List of documents to store.
            vectors (np.ndarray): Matrix of shape (n_documents, embedding_dim).
        """
        pass

    @abstractmethod
    def search(self, query_vector: np.ndarray, k: int = 5) -> List[Document]:
        """
        Search for the k most similar documents to the query vector.

        Args:
            query_vector (np.ndarray): Query vector of shape (embedding_dim,).
            k (int): Number of results to return. Defaults to 5.

        Returns:
            List[Document]: List of k most similar documents with updated metadata.
        """
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """
        Persist the vector store index and documents to disk.

        Args:
            path (str): Directory path where the store will be saved.
        """
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """
        Load the vector store index and documents from disk.

        Args:
            path (str): Directory path where the store was saved.
        """
        pass