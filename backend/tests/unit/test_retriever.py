"""
Tests for Retriever module 

"""

import pytest
import numpy as np
from unittest.mock import MagicMock

from src.loaders.base_loader import Document
from src.rag.retriever import Retriever


# Fixtures 

@pytest.fixture
def mock_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={"provider": "aws", "file_type": "pdf", "similarity_score": 0.92}
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={"provider": "aws", "file_type": "pdf", "similarity_score": 0.85}
        ),
        Document(
            content="Azure hybrid cloud enables seamless integration.",
            metadata={"provider": "azure", "file_type": "markdown", "similarity_score": 0.78}
        )
    ]


@pytest.fixture
def mock_embedder():
    embedder = MagicMock()
    embedder.embed_query.return_value = np.random.rand(384).astype("float32")
    return embedder


@pytest.fixture
def mock_vectorstore(mock_documents):
    vectorstore = MagicMock()
    vectorstore.search.return_value = mock_documents
    return vectorstore


@pytest.fixture
def retriever(mock_embedder, mock_vectorstore):
    return Retriever(embedder=mock_embedder, vectorstore=mock_vectorstore)


# Retriever.retrieve() 

class TestRetrieve:

    def test_retrieve_returns_documents(self, retriever):
        results = retriever.retrieve("What are AWS best practices?")
        assert len(results) > 0
        assert all(isinstance(r, Document) for r in results)

    def test_retrieve_calls_embed_query(self, retriever, mock_embedder):
        retriever.retrieve("What are AWS best practices?")
        mock_embedder.embed_query.assert_called_once_with("What are AWS best practices?")

    def test_retrieve_calls_search_with_correct_k(self, retriever, mock_vectorstore):
        retriever.retrieve("What are AWS best practices?", k=3)
        mock_vectorstore.search.assert_called_once()
        _, kwargs = mock_vectorstore.search.call_args
        assert kwargs["k"] == 3

    def test_retrieve_results_have_similarity_score(self, retriever):
        results = retriever.retrieve("What are AWS best practices?")
        for result in results:
            assert "similarity_score" in result.metadata

    def test_retrieve_results_have_content(self, retriever):
        results = retriever.retrieve("What are AWS best practices?")
        assert all(len(r.content.strip()) > 0 for r in results)

    def test_retrieve_default_k_is_5(self, retriever, mock_vectorstore):
        retriever.retrieve("What are AWS best practices?")
        _, kwargs = mock_vectorstore.search.call_args
        assert kwargs["k"] == 5