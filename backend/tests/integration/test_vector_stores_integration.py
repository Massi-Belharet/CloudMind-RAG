"""
Integration tests for vector stores 

Tests FAISS, Qdrant and Pgvector with real documents and embeddings
We need Docker to be running for Qdrant and Pgvector tests
"""

import pytest
import numpy as np
import psycopg2
from qdrant_client import QdrantClient

from src.loaders.base_loader import Document
from src.embeddings.embedder import Embedder
from src.vectorstores.faiss_store import FAISSStore
from src.vectorstores.qdrant_store import QdrantStore
from src.vectorstores.pgvector_store import PgvectorStore
from src.utils.settings import settings


# Fixtures 

@pytest.fixture(scope="module")
def embedder():
    return Embedder(model_name="all-MiniLM-L6-v2")


@pytest.fixture(scope="module")
def sample_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones for high availability.",
            metadata={"provider": "aws", "file_type": "pdf", "file_name": "aws.pdf"}
        ),
        Document(
            content="Cost optimization is a key pillar of the AWS Well-Architected Framework.",
            metadata={"provider": "aws", "file_type": "pdf", "file_name": "cost.pdf"}
        ),
        Document(
            content="Azure hybrid cloud enables seamless integration between on-premises and cloud.",
            metadata={"provider": "azure", "file_type": "pdf", "file_name": "azure.pdf"}
        ),
        Document(
            content="RGPD requires data residency compliance for European citizens data.",
            metadata={"provider": "compliance", "file_type": "pdf", "file_name": "rgpd.pdf"}
        ),
        Document(
            content="GCP recommends using Cloud Run for serverless containerized workloads.",
            metadata={"provider": "gcp", "file_type": "markdown", "file_name": "gcp.md"}
        )
    ]


@pytest.fixture(scope="module")
def vectors(embedder, sample_documents):
    return embedder.embed(sample_documents)


@pytest.fixture(scope="module")
def embedding_dim(vectors):
    return vectors.shape[1]


@pytest.fixture(scope="module")
def query_vector(embedder):
    return embedder.embed_query("What are the best practices for cost optimization?")


@pytest.fixture(scope="module", autouse=True)
def cleanup_qdrant():
    yield
    client = QdrantClient(host="localhost", port=6333)
    for collection in ["test_qdrant_integration", "test_compare_qdrant"]:
        if client.collection_exists(collection):
            client.delete_collection(collection)
            print(f"Collection '{collection}' deleted")



@pytest.fixture(scope="module", autouse=True)
def cleanup_pgvector():
    yield
    conn = psycopg2.connect(
        host=settings.postgres_host,
        port=settings.postgres_port,
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password
    )
    with conn.cursor() as cursor:
        for table in ["test_pgvector_integration", "test_compare_pgvector"]:
            cursor.execute(f"DROP TABLE IF EXISTS {table};")
    conn.commit()
    conn.close()
    print("Pgvector tables cleaned up")


# FAISS Integration 

@pytest.mark.integration
class TestFAISSIntegration:

    def test_faiss_add_and_search(self, sample_documents, vectors, query_vector, embedding_dim, tmp_path):
        store = FAISSStore(
            collection_name="test_faiss",
            embedding_dim=embedding_dim
        )
        store.add(sample_documents, vectors)
        results = store.search(query_vector, k=3)

        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)

    def test_faiss_results_have_similarity_score(self, sample_documents, vectors, query_vector, embedding_dim):
        store = FAISSStore(
            collection_name="test_faiss",
            embedding_dim=embedding_dim
        )
        store.add(sample_documents, vectors)
        results = store.search(query_vector, k=3)

        for result in results:
            assert "similarity_score" in result.metadata

    def test_faiss_save_and_load(self, sample_documents, vectors, query_vector, embedding_dim, tmp_path):
        store = FAISSStore(
            collection_name="test_faiss",
            embedding_dim=embedding_dim
        )
        store.add(sample_documents, vectors)
        store.save(str(tmp_path))

        new_store = FAISSStore(
            collection_name="test_faiss",
            embedding_dim=embedding_dim
        )
        new_store.load(str(tmp_path))
        results = new_store.search(query_vector, k=3)

        assert len(results) == 3


# Qdrant Integration 

@pytest.mark.integration
class TestQdrantIntegration:

    def test_qdrant_add_and_search(self, sample_documents, vectors, query_vector, embedding_dim):
        store = QdrantStore(
            collection_name="test_qdrant_integration",
            embedding_dim=embedding_dim
        )
        store.add(sample_documents, vectors)
        results = store.search(query_vector, k=3)

        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)

    def test_qdrant_results_have_similarity_score(self, sample_documents, vectors, query_vector, embedding_dim):
        store = QdrantStore(
            collection_name="test_qdrant_integration",
            embedding_dim=embedding_dim
        )
        results = store.search(query_vector, k=3)

        for result in results:
            assert "similarity_score" in result.metadata

    def test_qdrant_similarity_score_between_0_and_1(self, sample_documents, vectors, query_vector, embedding_dim):
        store = QdrantStore(
            collection_name="test_qdrant_integration",
            embedding_dim=embedding_dim
        )
        results = store.search(query_vector, k=3)

        for result in results:
            assert 0.0 <= result.metadata["similarity_score"] <= 1.0


# Pgvector Integration 

@pytest.mark.integration
class TestPgvectorIntegration:

    def test_pgvector_add_and_search(self, sample_documents, vectors, query_vector, embedding_dim):
        store = PgvectorStore(
            collection_name="test_pgvector_integration",
            embedding_dim=embedding_dim
        )
        store.add(sample_documents, vectors)
        results = store.search(query_vector, k=3)

        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)

    def test_pgvector_results_have_similarity_score(self, sample_documents, vectors, query_vector, embedding_dim):
        store = PgvectorStore(
            collection_name="test_pgvector_integration",
            embedding_dim=embedding_dim
        )
        results = store.search(query_vector, k=3)

        for result in results:
            assert "similarity_score" in result.metadata


# Cross-store Comparison 

@pytest.mark.integration
class TestCrossStoreComparison:

    def test_all_stores_return_same_top_provider(self, sample_documents, vectors, query_vector, embedding_dim, tmp_path):
        """All stores should agree on the most relevant provider for a given query."""

        faiss_store = FAISSStore(collection_name="test_compare_faiss", embedding_dim=embedding_dim)
        faiss_store.add(sample_documents, vectors)

        qdrant_store = QdrantStore(collection_name="test_compare_qdrant", embedding_dim=embedding_dim)
        qdrant_store.add(sample_documents, vectors)

        pgvector_store = PgvectorStore(collection_name="test_compare_pgvector", embedding_dim=embedding_dim)
        pgvector_store.add(sample_documents, vectors)

        faiss_top = faiss_store.search(query_vector, k=1)[0].metadata["provider"]
        qdrant_top = qdrant_store.search(query_vector, k=1)[0].metadata["provider"]
        pgvector_top = pgvector_store.search(query_vector, k=1)[0].metadata["provider"]

        assert faiss_top == qdrant_top == pgvector_top