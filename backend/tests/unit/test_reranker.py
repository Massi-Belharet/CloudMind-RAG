"""
Tests for Reranker module 

Covers rerank() with valid documents, score ordering, top_k limiting,
and metadata preservation using a mocked CrossEncoder.
"""

import pytest
from unittest.mock import MagicMock, patch

from src.loaders.base_loader import Document
from src.rag.reranker import Reranker


# Fixtures

@pytest.fixture
def sample_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={"provider": "aws", "file_type": "pdf"}
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={"provider": "aws", "file_type": "pdf"}
        ),
        Document(
            content="Azure hybrid cloud enables seamless integration.",
            metadata={"provider": "azure", "file_type": "pdf"}
        ),
        Document(
            content="GCP recommends Cloud Run for serverless workloads.",
            metadata={"provider": "gcp", "file_type": "markdown"}
        )
    ]


@pytest.fixture
def mock_cross_encoder():
    model = MagicMock()
    # Scores in reverse order — doc 4 most relevant, doc 1 least
    model.predict.return_value = [0.1, 0.4, 0.6, 0.9]
    return model


@pytest.fixture
def reranker(mock_cross_encoder):
    with patch("src.rag.reranker.CrossEncoder", return_value=mock_cross_encoder):
        return Reranker(model_name="test-model")


# Reranker.rerank()

class TestRerank:

    def test_rerank_returns_documents(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents, top_k=2)
        assert all(isinstance(r, Document) for r in results)

    def test_rerank_returns_top_k(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents, top_k=2)
        assert len(results) == 2

    def test_rerank_orders_by_score_descending(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents, top_k=4)
        
        # Highest score (0.9) corresponds to sample_documents[3]
        assert results[0].content == sample_documents[3].content
        assert results[-1].content == sample_documents[0].content

    def test_rerank_adds_rerank_score_to_metadata(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents, top_k=2)
        for r in results:
            assert "rerank_score" in r.metadata

    def test_rerank_preserves_existing_metadata(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents, top_k=2)
        for r in results:
            assert "provider" in r.metadata
            assert "file_type" in r.metadata

    def test_rerank_empty_documents(self, reranker):
        results = reranker.rerank("cloud cost optimization", [], top_k=5)
        assert results == []

    def test_rerank_uses_config_top_k_when_none(self, reranker, sample_documents):
        results = reranker.rerank("cloud cost optimization", sample_documents)
        assert len(results) == 5 or len(results) == len(sample_documents)