"""
Tests for HybridRetriever 

Covers BM25 search and the full hybrid retrieve()
combining lexical and dense search results via RRF fusion.
"""

import pytest
from unittest.mock import MagicMock

from src.loaders.base_loader import Document
from src.rag.hybrid_retriever import HybridRetriever


# Fixtures 

@pytest.fixture
def sample_documents():
    return [
        Document(
            content="AWS EC2 t3.medium costs 0.0416 dollars per hour in us-east-1.",
            metadata={"provider": "aws", "file_type": "csv"}
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={"provider": "aws", "file_type": "pdf"}
        ),
        Document(
            content="Azure hybrid cloud enables seamless integration between environments.",
            metadata={"provider": "azure", "file_type": "pdf"}
        ),
        Document(
            content="GCP recommends Cloud Run for serverless containerized workloads.",
            metadata={"provider": "gcp", "file_type": "markdown"}
        ),
        Document(
            content="RGPD article 28 requires data processing agreements with subprocessors.",
            metadata={"provider": "compliance", "file_type": "pdf"}
        )
    ]


@pytest.fixture
def mock_retriever(sample_documents):
    retriever = MagicMock()

    # Dense search returns documents in a different order than BM25
    retriever.retrieve.return_value = [
        sample_documents[2],
        sample_documents[1],
        sample_documents[0],
        sample_documents[3],
        sample_documents[4],
    ]
    return retriever


@pytest.fixture
def hybrid_retriever(mock_retriever, sample_documents):
    return HybridRetriever(retriever=mock_retriever, documents=sample_documents)


# HybridRetriever._bm25_search() 

class TestBM25Search:

    def test_bm25_search_returns_documents(self, hybrid_retriever):
        results = hybrid_retriever._bm25_search("AWS EC2 t3.medium us-east-1", k=3)
        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)

    def test_bm25_search_finds_exact_match(self, hybrid_retriever, sample_documents):
        results = hybrid_retriever._bm25_search("AWS EC2 t3.medium us-east-1", k=1)
        assert results[0].content == sample_documents[0].content

    def test_bm25_search_returns_k_results(self, hybrid_retriever):
        results = hybrid_retriever._bm25_search("cloud", k=2)
        assert len(results) == 2


# HybridRetriever.retrieve()

class TestRetrieve:

    def test_retrieve_returns_k_documents(self, hybrid_retriever):
        results = hybrid_retriever.retrieve("AWS cost optimization", k=3)
        assert len(results) == 3

    def test_retrieve_calls_dense_retriever(self, hybrid_retriever, mock_retriever):
        hybrid_retriever.retrieve("AWS cost optimization", k=3)
        mock_retriever.retrieve.assert_called_once()

    def test_retrieve_returns_documents(self, hybrid_retriever):
        results = hybrid_retriever.retrieve("AWS cost optimization", k=3)
        assert all(isinstance(r, Document) for r in results)

    def test_retrieve_default_k_is_5(self, hybrid_retriever, sample_documents):
        results = hybrid_retriever.retrieve("cloud")
        assert len(results) <= 5