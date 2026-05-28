"""
Base VectorStore module 

Defines two abstract interfaces following the Interface Segregation Principle:

- BaseVectorStore: core interface for all vector stores (add + search)
- PersistableStore: extended interface for stores that need disk persistence (FAISS)

Qdrant and Pgvector persist automatically — they implement BaseVectorStore only.
FAISS requires explicit save/load — it implements PersistableStore.

Functions:
    add(documents: List[Document], vectors: np.ndarray) -> None : Add documents and vectors.
    search(query_vector: np.ndarray, k: int) -> List[Document] : Search for k most similar documents.
    save(path: str) -> None : Persist the store to disk (PersistableStore only).
    load(path: str) -> None : Load the store from disk (PersistableStore only).
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
            List[Document]: List of k most similar documents.
        """
        pass


class PersistableStore(BaseVectorStore):

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

        Raises:
            FileNotFoundError: If the index or documents file does not exist.
        """
        pass