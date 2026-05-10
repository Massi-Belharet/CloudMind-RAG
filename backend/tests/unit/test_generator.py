"""
Tests for Generator module 

"""

import pytest
from unittest.mock import MagicMock, patch
from langchain_core.messages import AIMessage

from src.loaders.base_loader import Document
from src.llm.generator import Generator


# Fixtures

@pytest.fixture
def mock_llm():
    return MagicMock()


@pytest.fixture
def mock_chain():
    chain = MagicMock()
    chain.invoke.return_value = AIMessage(content="AWS recommends using multiple availability zones.")
    return chain


@pytest.fixture
def sample_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={
                "provider": "aws",
                "file_name": "aws-overview.pdf",
                "file_type": "pdf",
                "similarity_score": 0.92
            }
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={
                "provider": "azure",
                "file_name": "cost_model.pdf",
                "file_type": "pdf",
                "similarity_score": 0.85
            }
        ),
        Document(
            content="RGPD requires data residency compliance in Europe.",
            metadata={
                "provider": "compliance",
                "file_name": "rgpd_guidelines.pdf",
                "file_type": "pdf",
                "similarity_score": 0.78
            }
        )
    ]


@pytest.fixture
def generator(mock_llm):
    return Generator(llm=mock_llm)


# Generator.generate() 

class TestGenerate:

    def test_generate_returns_string(self, generator, sample_documents, mock_chain):
        with patch("src.llm.generator.get_rag_prompt") as mock_prompt:
            mock_prompt.return_value.__or__ = MagicMock(return_value=mock_chain)
            response = generator.generate("What are AWS best practices?", sample_documents)
            assert isinstance(response, str)

    def test_generate_returns_non_empty_response(self, generator, sample_documents, mock_chain):
        with patch("src.llm.generator.get_rag_prompt") as mock_prompt:
            mock_prompt.return_value.__or__ = MagicMock(return_value=mock_chain)
            response = generator.generate("What are AWS best practices?", sample_documents)
            assert len(response.strip()) > 0

    def test_generate_calls_chain(self, generator, sample_documents, mock_chain):
        with patch("src.llm.generator.get_rag_prompt") as mock_prompt:
            mock_prompt.return_value.__or__ = MagicMock(return_value=mock_chain)
            generator.generate("What are AWS best practices?", sample_documents)
            mock_chain.invoke.assert_called_once()

    def test_generate_with_empty_documents(self, generator, mock_chain):
        with patch("src.llm.generator.get_rag_prompt") as mock_prompt:
            mock_prompt.return_value.__or__ = MagicMock(return_value=mock_chain)
            response = generator.generate("What are AWS best practices?", [])
            assert isinstance(response, str)


# Generator._build_context() 

class TestBuildContext:

    def test_build_context_returns_string(self, generator, sample_documents):
        context = generator._build_context(sample_documents)
        assert isinstance(context, str)

    def test_build_context_includes_provider(self, generator, sample_documents):
        context = generator._build_context(sample_documents)
        assert "AWS" in context
        assert "AZURE" in context
        assert "COMPLIANCE" in context

    def test_build_context_includes_source(self, generator, sample_documents):
        context = generator._build_context(sample_documents)
        assert "aws-overview.pdf" in context
        assert "cost_model.pdf" in context

    def test_build_context_includes_content(self, generator, sample_documents):
        context = generator._build_context(sample_documents)
        assert "AWS recommends using multiple availability zones." in context
        assert "Cost optimization is a key pillar" in context

    def test_build_context_numbered_sources(self, generator, sample_documents):
        context = generator._build_context(sample_documents)
        assert "[1]" in context
        assert "[2]" in context
        assert "[3]" in context

    def test_build_context_empty_documents(self, generator):
        context = generator._build_context([])
        assert context == ""