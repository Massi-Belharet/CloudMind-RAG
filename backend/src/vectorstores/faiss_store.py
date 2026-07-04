"""
FAISS Vector Store module

Implements BaseVectorStore using FAISS IndexHNSWFlat with cosine similarity
for efficient similarity search. Vectors are normalized before indexing to
ensure cosine similarity via inner product. Used in Sprint 1 for Naive RAG
pipeline before benchmarking against Qdrant and Pgvector in Sprint 2.

Functions:
    add(documents: List[Document], vectors: np.ndarray) -> None : Add documents and vectors to the index.
    search(query_vector: np.ndarray, k: int, filter_provider: Optional[str]) -> List[Document] : Search for k most similar documents.
    save(path: str) -> None : Persist index and documents to disk.
    load(path: str) -> None : Load index and documents from disk.
"""

import os
import json
from typing import List, Optional
import numpy as np
import faiss

from src.loaders.base_loader import Document
from src.vectorstores.base_vectorstore import PersistableStore


class FAISSStore(PersistableStore):

    def __init__(self, collection_name: str, embedding_dim: int, M: int = 32):
        """
        Initialize FAISSStore with HNSW index.

        Args:
            collection_name (str): Name of the collection.
            embedding_dim (int): Dimension of the embedding vectors.
            M (int): Number of neighbors in HNSW graph. 
        """
        super().__init__(collection_name)
        self.embedding_dim = embedding_dim
        self.M = M
        self.index = faiss.IndexHNSWFlat(embedding_dim, M, faiss.METRIC_INNER_PRODUCT)
        self.documents: List[Document] = []

    def add(self, documents: List[Document], vectors: np.ndarray) -> None:
        """
        Add documents and their vectors to the HNSW index.
        Vectors are normalized to enable cosine similarity via inner product.

        Args:
            documents (List[Document]): List of documents to store.
            vectors (np.ndarray): Matrix of shape (n_documents, embedding_dim).
        """
        vectors = np.array(vectors).astype("float32")
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.documents.extend(documents)

    def search(self, query_vector: np.ndarray, k: int = 5, filter_provider: Optional[str] = None) -> List[Document]:
        """
        Search for the k most similar documents to the query vector.
        Query vector is normalized before search for cosine similarity.

        Args:
            query_vector (np.ndarray): Query vector of shape (embedding_dim,).
            k (int): Number of results to return.
            filter_provider (Optional[str]): Accepted for interface consistency with
                BaseVectorStore. Not implemented for FAISS (not used in production) —
                must be None.

        Returns:
            List[Document]: List of k most similar documents with similarity score in metadata.

        Raises:
            NotImplementedError: If filter_provider is set.
        """
        if filter_provider is not None:
            raise NotImplementedError("Provider filtering is not implemented for FAISSStore.")

        query = np.array([query_vector]).astype("float32")
        faiss.normalize_L2(query)
        distances, indices = self.index.search(query, k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx == -1:
                continue
            doc = self.documents[idx]
            results.append(Document(
                content=doc.content,
                metadata={
                    **doc.metadata,
                    "similarity_score": float(distances[0][i])
                }
            ))

        return results

    def save(self, path: str) -> None:
        """
        Persist the HNSW index and documents to disk.

        Args:
            path (str): Directory path where the store will be saved.
        """
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, os.path.join(path, f"{self.collection_name}.index"))

        docs_serializable = [
            {"content": doc.content, "metadata": doc.metadata}
            for doc in self.documents
        ]
        with open(os.path.join(path, f"{self.collection_name}.json"), "w") as f:
            json.dump(docs_serializable, f)

    def load(self, path: str) -> None:
        """
        Load the HNSW index and documents from disk.

        Args:
            path (str): Directory path where the store was saved.

        Raises:
            FileNotFoundError: If the index or documents file does not exist.
        """
        index_path = os.path.join(path, f"{self.collection_name}.index")
        docs_path = os.path.join(path, f"{self.collection_name}.json")

        if not os.path.exists(index_path) or not os.path.exists(docs_path):
            raise FileNotFoundError(f"No saved store found at {path}")

        self.index = faiss.read_index(index_path)

        with open(docs_path, "r") as f:
            docs_data = json.load(f)

        self.documents = [
            Document(content=d["content"], metadata=d["metadata"])
            for d in docs_data
        ]