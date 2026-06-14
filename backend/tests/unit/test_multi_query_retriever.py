"""
Tests for MultiQueryRetriever module 

Covers query reformulation generation, RAG-Fusion retrieval combining
the original query with LLM-generated variants via RRF, and config defaults.
"""

import pytest
from unittest.mock import MagicMock

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage

from src.loaders.base_loader import Document
from src.rag.multi_query_retriever import MultiQueryRetriever
from src.utils.config import config


# Fixtures

@pytest.fixture
def sample_documents():
    return [
        Document(content="AWS EC2 cost optimization with reserved instances.", metadata={"provider": "aws"}),
        Document(content="Azure cost management best practices.", metadata={"provider": "azure"}),
        Document(content="GCP billing export to BigQuery for FinOps analysis.", metadata={"provider": "gcp"}),
        Document(content="RGPD compliance for cloud data residency.", metadata={"provider": "compliance"}),
        Document(content="Multi-cloud architecture design patterns.", metadata={"provider": "general"}),
    ]


@pytest.fixture
def mock_llm():
    llm = MagicMock(spec=BaseChatModel)
    llm.invoke.return_value = AIMessage(content="Reformulation one\nReformulation two\nReformulation three")
    return llm


@pytest.fixture
def mock_hybrid_retriever(sample_documents):
    retriever = MagicMock()
    retriever.retrieve.return_value = sample_documents[:3]
    return retriever


@pytest.fixture
def multi_query_retriever(mock_llm, mock_hybrid_retriever):
    return MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid_retriever, n_queries=3)


# MultiQueryRetriever._generate_queries() 

class TestGenerateQueries:

    def test_generate_queries_returns_list_of_strings(self, multi_query_retriever):
        reformulations = multi_query_retriever._generate_queries("original query")
        assert reformulations == ["Reformulation one", "Reformulation two", "Reformulation three"]

    def test_generate_queries_filters_empty_lines(self, mock_llm, mock_hybrid_retriever):
        mock_llm.invoke.return_value = AIMessage(content="Reform 1\n\nReform 2\n\n")
        retriever = MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid_retriever, n_queries=3)

        reformulations = retriever._generate_queries("original query")
        assert reformulations == ["Reform 1", "Reform 2"]

    def test_generate_queries_limits_to_n_queries(self, mock_llm, mock_hybrid_retriever):
        mock_llm.invoke.return_value = AIMessage(content="Q1\nQ2\nQ3\nQ4\nQ5")
        retriever = MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid_retriever, n_queries=3)

        reformulations = retriever._generate_queries("original query")
        assert len(reformulations) == 3


# MultiQueryRetriever.retrieve() 

class TestRetrieve:

    def test_retrieve_returns_documents(self, multi_query_retriever):
        results = multi_query_retriever.retrieve("original query", k=3)
        assert all(isinstance(r, Document) for r in results)

    def test_retrieve_returns_k_documents(self, multi_query_retriever):
        results = multi_query_retriever.retrieve("original query", k=2)
        assert len(results) == 2

    def test_retrieve_default_k_is_5(self, multi_query_retriever):
        results = multi_query_retriever.retrieve("original query")
        assert len(results) <= 5

    def test_retrieve_calls_retriever_for_each_query_variant(self, multi_query_retriever, mock_hybrid_retriever):
        multi_query_retriever.retrieve("original query", k=3)
        # 1 original query + 3 reformulations = 4 calls
        assert mock_hybrid_retriever.retrieve.call_count == 4

    def test_retrieve_includes_original_query(self, multi_query_retriever, mock_hybrid_retriever):
        multi_query_retriever.retrieve("original query", k=3)
        called_queries = [call.args[0] for call in mock_hybrid_retriever.retrieve.call_args_list]
        assert "original query" in called_queries

    def test_retrieve_fuses_results_from_all_variants(self, mock_llm, sample_documents):
        mock_hybrid = MagicMock()
        # sample_documents[0] appears in results for the original query AND reformulation one
        mock_hybrid.retrieve.side_effect = [
            [sample_documents[0], sample_documents[1]],
            [sample_documents[0], sample_documents[2]],
            [sample_documents[3]],
            [sample_documents[4]],
        ]
        retriever = MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid, n_queries=3)

        results = retriever.retrieve("original query", k=1)
        # sample_documents[0] appears in 2 of the 4 ranked lists → ranks first after RRF
        assert results[0].content == sample_documents[0].content

    def test_retrieve_with_no_reformulations(self, mock_llm, mock_hybrid_retriever):
        mock_llm.invoke.return_value = AIMessage(content="")
        retriever = MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid_retriever, n_queries=3)

        results = retriever.retrieve("original query", k=2)
        # Only the original query is searched
        assert mock_hybrid_retriever.retrieve.call_count == 1
        assert len(results) == 2


# MultiQueryRetriever — config defaults 

class TestConfigDefaults:

    def test_uses_config_n_queries_when_none(self, mock_llm, mock_hybrid_retriever):
        retriever = MultiQueryRetriever(llm=mock_llm, retriever=mock_hybrid_retriever)
        assert retriever.n_queries == config.multi_query.n_queries