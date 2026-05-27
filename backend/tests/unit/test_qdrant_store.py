"""
Tests for QdrantStore module in CloudMind RAG pipeline.

Covers add(), search(), save(), load() and collection creation
using a mocked QdrantClient to avoid requiring a running Qdrant instance.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock, patch

from src.loaders.base_loader import Document
from src.vectorstores.qdrant_store import QdrantStore


# Fixtures 

@pytest.fixture
def embedding_dim():
    return 384


@pytest.fixture
def sample_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={"provider": "aws", "file_type": "pdf", "file_name": "aws.pdf"}
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={"provider": "azure", "file_type": "pdf", "file_name": "cost.pdf"}
        ),
        Document(
            content="RGPD requires data residency compliance in Europe.",
            metadata={"provider": "compliance", "file_type": "pdf", "file_name": "rgpd.pdf"}
        )
    ]


@pytest.fixture
def sample_vectors(embedding_dim):
    np.random.seed(42)
    return np.random.rand(3, embedding_dim).astype("float32")


@pytest.fixture
def query_vector(embedding_dim):
    np.random.seed(99)
    return np.random.rand(embedding_dim).astype("float32")


@pytest.fixture
def mock_client():
    client = MagicMock()
    client.collection_exists.return_value = False
    return client


@pytest.fixture
def store(mock_client, embedding_dim):
    return QdrantStore(
        collection_name="test_collection",
        embedding_dim=embedding_dim,
        client=mock_client
    )


# QdrantStore.__init__ 

class TestInit:

    def test_collection_created_if_not_exists(self, mock_client, embedding_dim):
        mock_client.collection_exists.return_value = False
        QdrantStore(
            collection_name="test",
            embedding_dim=embedding_dim,
            client=mock_client
        )
        mock_client.create_collection.assert_called_once()

    def test_collection_not_created_if_exists(self, mock_client, embedding_dim):
        mock_client.collection_exists.return_value = True
        QdrantStore(
            collection_name="test",
            embedding_dim=embedding_dim,
            client=mock_client
        )
        mock_client.create_collection.assert_not_called()


# QdrantStore.add()

class TestAdd:

    def test_add_calls_upsert(self, store, mock_client, sample_documents, sample_vectors):
        store.add(sample_documents, sample_vectors)
        mock_client.upsert.assert_called()

    def test_add_correct_number_of_points(self, store, mock_client, sample_documents, sample_vectors):
        store.add(sample_documents, sample_vectors)
        total_points = sum(
            len(call.kwargs["points"])
            for call in mock_client.upsert.call_args_list
        )
        assert total_points == len(sample_documents)

    def test_add_points_have_content_in_payload(self, store, mock_client, sample_documents, sample_vectors):
        store.add(sample_documents, sample_vectors)
        points = mock_client.upsert.call_args_list[0].kwargs["points"]
        for point in points:
            assert "content" in point.payload

    def test_add_points_have_metadata_in_payload(self, store, mock_client, sample_documents, sample_vectors):
        store.add(sample_documents, sample_vectors)
        points = mock_client.upsert.call_args_list[0].kwargs["points"]
        for point in points:
            assert "provider" in point.payload
            assert "file_type" in point.payload


# QdrantStore.search() 

class TestSearch:

    def test_search_returns_documents(self, store, mock_client, query_vector):
        mock_point = MagicMock()
        mock_point.payload = {
            "content": "AWS recommends high availability.",
            "provider": "aws",
            "file_type": "pdf"
        }
        mock_point.score = 0.92
        mock_client.query_points.return_value.points = [mock_point]

        results = store.search(query_vector, k=1)
        assert len(results) == 1
        assert isinstance(results[0], Document)

    def test_search_results_have_content(self, store, mock_client, query_vector):
        mock_point = MagicMock()
        mock_point.payload = {
            "content": "AWS recommends high availability.",
            "provider": "aws",
            "file_type": "pdf"
        }
        mock_point.score = 0.92
        mock_client.query_points.return_value.points = [mock_point]

        results = store.search(query_vector, k=1)
        assert results[0].content == "AWS recommends high availability."

    def test_search_results_have_similarity_score(self, store, mock_client, query_vector):
        mock_point = MagicMock()
        mock_point.payload = {
            "content": "AWS recommends high availability.",
            "provider": "aws",
            "file_type": "pdf"
        }
        mock_point.score = 0.92
        mock_client.query_points.return_value.points = [mock_point]

        results = store.search(query_vector, k=1)
        assert "similarity_score" in results[0].metadata
        assert results[0].metadata["similarity_score"] == 0.92

    def test_search_calls_query_points_with_correct_limit(self, store, mock_client, query_vector):
        mock_client.query_points.return_value.points = []
        store.search(query_vector, k=3)
        mock_client.query_points.assert_called_once_with(
            collection_name="test_collection",
            query=query_vector.tolist(),
            limit=3
        )


# QdrantStore.save() and load()

class TestSaveLoad:

    def test_save_raises_if_collection_not_exists(self, store, mock_client):
        mock_client.collection_exists.return_value = False
        with pytest.raises(ValueError):
            store.save("unused_path")

    def test_save_succeeds_if_collection_exists(self, store, mock_client):
        mock_client.collection_exists.return_value = True
        store.save("unused_path")

    def test_load_raises_if_collection_not_exists(self, store, mock_client):
        mock_client.collection_exists.return_value = False
        with pytest.raises(ValueError):
            store.load("unused_path")

    def test_load_succeeds_if_collection_exists(self, store, mock_client):
        mock_client.collection_exists.return_value = True
        store.load("unused_path")