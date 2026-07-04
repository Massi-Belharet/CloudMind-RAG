"""
Pgvector Vector Store module 

Implements BaseVectorStore using PostgreSQL 
Vectors are stored in a dedicated table with document content and metadata


Functions:
    _create_table_if_not_exists() -> None : Create the vectors table if it does not exist.
    add(documents: List[Document], vectors: np.ndarray) -> None : Add documents and vectors to the table.
    search(query_vector: np.ndarray, k: int, filter_provider: Optional[str]) -> List[Document] : Search for k most similar documents.
"""

import json
from typing import List, Optional
import numpy as np
import psycopg2
from psycopg2.extras import execute_values
from pgvector.psycopg2 import register_vector

from src.loaders.base_loader import Document
from src.vectorstores.base_vectorstore import BaseVectorStore
from src.utils.settings import settings


class PgvectorStore(BaseVectorStore):

    def __init__(self, collection_name: str, embedding_dim: int, connection=None):
        """
        Initialize PgvectorStore and connect to PostgreSQL.
        Connection settings are loaded from .env via Pydantic Settings.

        Args:
            collection_name (str): Name of the table to store vectors in.
            embedding_dim (int): Dimension of the embedding vectors.
            connection: Optional psycopg2 connection for testing (dependency injection).
        """
        super().__init__(collection_name)
        self.embedding_dim = embedding_dim
        self.connection = connection or psycopg2.connect(
            host=settings.postgres_host,
            port=settings.postgres_port,
            dbname=settings.postgres_db,
            user=settings.postgres_user,
            password=settings.postgres_password
        )
        register_vector(self.connection)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        """
        Create the vectors table and HNSW index if they do not already exist.
        Uses HNSW index for cosine similarity — works on empty tables unlike ivfflat.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.collection_name} (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    metadata JSONB,
                    embedding vector({self.embedding_dim})
                );
            """)
            cursor.execute(f"""
                CREATE INDEX IF NOT EXISTS {self.collection_name}_embedding_idx
                ON {self.collection_name}
                USING hnsw (embedding vector_cosine_ops);
            """)
        self.connection.commit()
        print(f"Table '{self.collection_name}' ready")

    def add(self, documents: List[Document], vectors: np.ndarray) -> None:
        """
        Add documents and their vectors to the PostgreSQL table.

        Args:
            documents (List[Document]): List of documents to store.
            vectors (np.ndarray): Matrix of shape (n_documents, embedding_dim).
        """
        rows = []
        for doc, vector in zip(documents, vectors):
            rows.append((
                doc.content,
                json.dumps(doc.metadata),
                vector.tolist()
            ))

        with self.connection.cursor() as cursor:
            execute_values(
                cursor,
                f"""
                INSERT INTO {self.collection_name} (content, metadata, embedding)
                VALUES %s
                """,
                rows
            )
        self.connection.commit()
        print(f"{len(rows)} rows inserted into '{self.collection_name}'")

    def search(self, query_vector: np.ndarray, k: int = 5, filter_provider: Optional[str] = None) -> List[Document]:
        """
        Search for the k most similar documents using cosine similarity.

        Args:
            query_vector (np.ndarray): Query vector of shape (embedding_dim,).
            k (int): Number of results to return. Defaults to 5.
            filter_provider (Optional[str]): Accepted for interface consistency with
                BaseVectorStore. Not implemented for Pgvector (not used in production) —
                must be None.

        Returns:
            List[Document]: List of k most similar documents with similarity score in metadata.

        Raises:
            NotImplementedError: If filter_provider is set.
        """
        if filter_provider is not None:
            raise NotImplementedError("Provider filtering is not implemented for PgvectorStore.")

        query_list = query_vector.tolist()

        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""
                SELECT content, metadata,
                       1 - (embedding <=> %s::vector) AS similarity_score
                FROM {self.collection_name}
                ORDER BY embedding <=> %s::vector
                LIMIT %s;
                """,
                (query_list, query_list, k)
            )
            results = cursor.fetchall()

        documents = []
        for content, metadata, similarity_score in results:
            meta = metadata if isinstance(metadata, dict) else json.loads(metadata)
            meta["similarity_score"] = similarity_score
            documents.append(Document(content=content, metadata=meta))

        return documents