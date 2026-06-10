"""
Tests for PgvectorStore 

Covers _create_table_if_not_exists(), add() and search()
using a mocked psycopg2 connection to avoid requiring a running PostgreSQL instance.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock, patch

from src.loaders.base_loader import Document
from src.vectorstores.pgvector_store import PgvectorStore


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
        )
    ]


@pytest.fixture
def sample_vectors(embedding_dim):
    np.random.seed(42)
    return np.random.rand(2, embedding_dim).astype("float32")


@pytest.fixture
def query_vector(embedding_dim):
    np.random.seed(99)
    return np.random.rand(embedding_dim).astype("float32")


@pytest.fixture
def mock_cursor():
    cursor = MagicMock()
    cursor.fetchall.return_value = []
    return cursor


@pytest.fixture
def mock_connection(mock_cursor):
    connection = MagicMock()
    connection.cursor.return_value.__enter__ = MagicMock(return_value=mock_cursor)
    connection.cursor.return_value.__exit__ = MagicMock(return_value=False)
    return connection


@pytest.fixture
def store(mock_connection, embedding_dim):
    with patch("src.vectorstores.pgvector_store.register_vector"):
        return PgvectorStore(
            collection_name="test_collection",
            embedding_dim=embedding_dim,
            connection=mock_connection
        )


# PgvectorStore._create_table_if_not_exists() 

class TestInit:

    def test_create_table_called_on_init(self, mock_connection, mock_cursor, embedding_dim):
        with patch("src.vectorstores.pgvector_store.register_vector"):
            PgvectorStore(
                collection_name="test_collection",
                embedding_dim=embedding_dim,
                connection=mock_connection
            )
        assert mock_cursor.execute.called

    def test_commit_called_after_table_creation(self, mock_connection, embedding_dim):
        with patch("src.vectorstores.pgvector_store.register_vector"):
            PgvectorStore(
                collection_name="test_collection",
                embedding_dim=embedding_dim,
                connection=mock_connection
            )
        mock_connection.commit.assert_called()


# PgvectorStore.add() 

class TestAdd:

    def test_add_commits_after_insert(self, store, mock_connection, sample_documents, sample_vectors):
        with patch("src.vectorstores.pgvector_store.execute_values"):
            store.add(sample_documents, sample_vectors)
        mock_connection.commit.assert_called()

    def test_add_calls_execute_values(self, store, sample_documents, sample_vectors):
        with patch("src.vectorstores.pgvector_store.execute_values") as mock_execute:
            store.add(sample_documents, sample_vectors)
            mock_execute.assert_called_once()

    def test_add_correct_number_of_rows(self, store, sample_documents, sample_vectors):
        captured_rows = []

        def capture_execute_values(cursor, query, rows):
            captured_rows.extend(rows)

        with patch("src.vectorstores.pgvector_store.execute_values", side_effect=capture_execute_values):
            store.add(sample_documents, sample_vectors)

        assert len(captured_rows) == len(sample_documents)

    def test_add_rows_have_content(self, store, sample_documents, sample_vectors):
        captured_rows = []

        def capture_execute_values(cursor, query, rows):
            captured_rows.extend(rows)

        with patch("src.vectorstores.pgvector_store.execute_values", side_effect=capture_execute_values):
            store.add(sample_documents, sample_vectors)

        for row in captured_rows:
            assert row[0] in [doc.content for doc in sample_documents]


# PgvectorStore.search() 

class TestSearch:

    def test_search_returns_empty_list_when_no_results(self, store, mock_cursor, query_vector):
        mock_cursor.fetchall.return_value = []
        results = store.search(query_vector, k=5)
        assert results == []

    def test_search_returns_documents(self, store, mock_cursor, query_vector):
        mock_cursor.fetchall.return_value = [
            ("AWS recommends high availability.", {"provider": "aws", "file_type": "pdf"}, 0.92),
        ]
        results = store.search(query_vector, k=1)
        assert len(results) == 1
        assert isinstance(results[0], Document)

    def test_search_results_have_content(self, store, mock_cursor, query_vector):
        mock_cursor.fetchall.return_value = [
            ("AWS recommends high availability.", {"provider": "aws", "file_type": "pdf"}, 0.92),
        ]
        results = store.search(query_vector, k=1)
        assert results[0].content == "AWS recommends high availability."

    def test_search_results_have_similarity_score(self, store, mock_cursor, query_vector):
        mock_cursor.fetchall.return_value = [
            ("AWS recommends high availability.", {"provider": "aws", "file_type": "pdf"}, 0.92),
        ]
        results = store.search(query_vector, k=1)
        assert "similarity_score" in results[0].metadata
        assert results[0].metadata["similarity_score"] == 0.92

    def test_search_preserves_metadata(self, store, mock_cursor, query_vector):
        mock_cursor.fetchall.return_value = [
            ("AWS recommends high availability.", {"provider": "aws", "file_type": "pdf"}, 0.92),
        ]
        results = store.search(query_vector, k=1)
        assert results[0].metadata["provider"] == "aws"
        assert results[0].metadata["file_type"] == "pdf"