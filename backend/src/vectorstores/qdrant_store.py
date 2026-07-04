"""
Qdrant Vector Store module

Implements BaseVectorStore using Qdrant as a persistent vector database.
Each document is stored as a Qdrant point with its metadata as payload, enabling rich filtering capabilities.

Functions:
    _create_collection_if_not_exists() -> None : Create Qdrant collection if it does not exist.
    add(documents: List[Document], vectors: np.ndarray) -> None : Add documents and vectors to the collection in batches.
    search(query_vector: np.ndarray, k: int, filter_provider: Optional[str]) -> List[Document] : Search for k most similar documents, optionally restricted to one provider.
    save(path: str) -> None : Verify collection exists in Qdrant.
    load(path: str) -> None : Verify collection exists and is ready to query.
"""

from typing import List, Optional
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

from src.loaders.base_loader import Document
from src.vectorstores.base_vectorstore import BaseVectorStore
from src.utils.settings import settings


class QdrantStore(BaseVectorStore):

    def __init__(self, collection_name: str, embedding_dim: int, batch_size: int = 100, client: QdrantClient = None):
        """
        Initialize QdrantStore and connect to a running Qdrant instance.

        Args:
            collection_name (str): Name of the Qdrant collection.
            embedding_dim (int): Dimension of the embedding vectors.
            batch_size (int): Number of points per upsert batch. Defaults to 100.
        """
        super().__init__(collection_name)
        self.embedding_dim = embedding_dim
        self.batch_size = batch_size
        self.client = client or QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self) -> None:
        """
        Create the Qdrant collection if it does not already exist.
        Uses cosine similarity — Qdrant normalizes vectors automatically.
        """
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.embedding_dim,
                    distance=Distance.COSINE
                )
            )
            print(f"Collection '{self.collection_name}' created")
        else:
            print(f"Collection '{self.collection_name}' already exists")

    def add(self, documents: List[Document], vectors: np.ndarray) -> None:
        """
        Add documents and their vectors to the Qdrant collection in batches.

        Args:
            documents (List[Document]): List of documents to store.
            vectors (np.ndarray): Matrix of shape (n_documents, embedding_dim).
        """
        points = []
        for idx, (doc, vector) in enumerate(zip(documents, vectors)):
            points.append(PointStruct(
                id=idx,
                vector=vector.tolist(),
                payload={"content": doc.content, **doc.metadata}
            ))

        for i in range(0, len(points), self.batch_size):
            batch = points[i:i + self.batch_size]
            self.client.upsert(
                collection_name=self.collection_name,
                points=batch
            )

        print(f"{len(points)} points added to '{self.collection_name}'")

    def search(self, query_vector: np.ndarray, k: int = 5, filter_provider: Optional[str] = None) -> List[Document]:
        """
        Search for the k most similar documents to the query vector.

        Args:
            query_vector (np.ndarray): Query vector of shape (embedding_dim,).
            k (int): Number of results to return. Defaults to 5.
            filter_provider (Optional[str]): If set, restrict results to chunks whose
                'provider' payload field matches this value. Defaults to None, which
                performs an unfiltered search across all providers (unchanged behavior).

        Returns:
            List[Document]: List of k most similar documents with similarity score in metadata.
        """
        query_filter = None
        if filter_provider is not None:
            query_filter = Filter(
                must=[FieldCondition(key="provider", match=MatchValue(value=filter_provider))]
            )

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector.tolist(),
            limit=k,
            query_filter=query_filter
        )

        documents = []
        for point in results.points:
            payload = point.payload.copy()
            content = payload.pop("content")
            payload["similarity_score"] = point.score

            documents.append(Document(
                content=content,
                metadata=payload
            ))

        return documents
