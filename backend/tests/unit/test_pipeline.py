"""
Tests for Pipeline module 
"""

import pytest
from unittest.mock import MagicMock
import numpy as np

from src.loaders.base_loader import Document
from src.rag.pipeline import Pipeline
from src.rag.reranker import Reranker
from src.vectorstores.base_vectorstore import PersistableStore


# Fixtures 

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
def sample_chunks():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={"provider": "aws", "file_type": "pdf", "chunk_index": 0, "chunk_total": 1}
        )
    ]


@pytest.fixture
def mock_loader(sample_documents):
    loader = MagicMock()
    loader.load.return_value = sample_documents
    return loader


@pytest.fixture
def mock_cleaner(sample_documents):
    cleaner = MagicMock()
    cleaner.clean.return_value = sample_documents
    return cleaner


@pytest.fixture
def mock_splitter(sample_chunks):
    splitter = MagicMock()
    splitter.split.return_value = sample_chunks
    return splitter


@pytest.fixture
def mock_embedder(sample_chunks):
    embedder = MagicMock()
    embedder.embed.return_value = np.random.rand(len(sample_chunks), 384).astype("float32")
    return embedder


@pytest.fixture
def mock_vectorstore():
    return MagicMock()


@pytest.fixture
def mock_persistable_vectorstore():
    return MagicMock(spec=PersistableStore)


@pytest.fixture
def mock_retriever(sample_chunks):
    retriever = MagicMock()
    retriever.retrieve.return_value = sample_chunks
    return retriever


@pytest.fixture
def mock_generator():
    generator = MagicMock()
    generator.generate.return_value = "AWS recommends multiple availability zones for high availability."
    return generator


@pytest.fixture
def mock_reranker(sample_chunks):
    reranker = MagicMock(spec=Reranker)
    reranker.rerank.return_value = sample_chunks
    return reranker


@pytest.fixture
def pipeline(mock_loader, mock_cleaner, mock_splitter, mock_embedder, mock_vectorstore, mock_retriever, mock_generator):
    return Pipeline(
        loaders=[mock_loader],
        cleaner=mock_cleaner,
        splitter=mock_splitter,
        embedder=mock_embedder,
        vectorstore=mock_vectorstore,
        retriever=mock_retriever,
        generator=mock_generator,
        storage_path="backend/data/processed/faiss"
    )


@pytest.fixture
def pipeline_with_reranker(mock_loader, mock_cleaner, mock_splitter, mock_embedder, mock_vectorstore, mock_retriever, mock_generator, mock_reranker):
    return Pipeline(
        loaders=[mock_loader],
        cleaner=mock_cleaner,
        splitter=mock_splitter,
        embedder=mock_embedder,
        vectorstore=mock_vectorstore,
        retriever=mock_retriever,
        generator=mock_generator,
        reranker=mock_reranker,
        storage_path="backend/data/processed/faiss"
    )


# Pipeline.build() 

class TestBuild:

    def test_build_calls_loader(self, pipeline, mock_loader):
        pipeline.build()
        mock_loader.load.assert_called_once()

    def test_build_calls_cleaner(self, pipeline, mock_cleaner):
        pipeline.build()
        mock_cleaner.clean.assert_called_once()

    def test_build_calls_splitter(self, pipeline, mock_splitter):
        pipeline.build()
        mock_splitter.split.assert_called_once()

    def test_build_calls_embedder(self, pipeline, mock_embedder):
        pipeline.build()
        mock_embedder.embed.assert_called_once()

    def test_build_calls_vectorstore_add(self, pipeline, mock_vectorstore):
        pipeline.build()
        mock_vectorstore.add.assert_called_once()

    def test_build_does_not_save_non_persistable_store(self, pipeline, mock_vectorstore):
        pipeline.build()
        mock_vectorstore.save.assert_not_called()

    def test_build_saves_persistable_store(self, mock_loader, mock_cleaner, mock_splitter, mock_embedder, mock_persistable_vectorstore, mock_retriever, mock_generator):
        mock_persistable_vectorstore.add.return_value = None
        pipeline = Pipeline(
            loaders=[mock_loader],
            cleaner=mock_cleaner,
            splitter=mock_splitter,
            embedder=mock_embedder,
            vectorstore=mock_persistable_vectorstore,
            retriever=mock_retriever,
            generator=mock_generator,
            storage_path="backend/data/processed/faiss"
        )
        pipeline.build()
        mock_persistable_vectorstore.save.assert_called_once_with("backend/data/processed/faiss")

    def test_build_multiple_loaders(self, mock_cleaner, mock_splitter, mock_embedder, mock_vectorstore, mock_retriever, mock_generator, sample_documents):
        loader1 = MagicMock()
        loader2 = MagicMock()
        loader1.load.return_value = sample_documents
        loader2.load.return_value = sample_documents

        pipeline = Pipeline(
            loaders=[loader1, loader2],
            cleaner=mock_cleaner,
            splitter=mock_splitter,
            embedder=mock_embedder,
            vectorstore=mock_vectorstore,
            retriever=mock_retriever,
            generator=mock_generator
        )
        pipeline.build()
        loader1.load.assert_called_once()
        loader2.load.assert_called_once()


# Pipeline.ask() 

class TestAsk:

    def test_ask_returns_string(self, pipeline):
        response = pipeline.ask("What are AWS best practices?")
        assert isinstance(response, str)

    def test_ask_returns_non_empty_response(self, pipeline):
        response = pipeline.ask("What are AWS best practices?")
        assert len(response.strip()) > 0

    def test_ask_calls_retriever(self, pipeline, mock_retriever):
        pipeline.ask("What are AWS best practices?", k=3)
        mock_retriever.retrieve.assert_called_once_with("What are AWS best practices?", k=3)

    def test_ask_calls_generator(self, pipeline, mock_generator):
        pipeline.ask("What are AWS best practices?")
        mock_generator.generate.assert_called_once()

    def test_ask_default_k_is_5(self, pipeline, mock_retriever):
        pipeline.ask("What are AWS best practices?")
        mock_retriever.retrieve.assert_called_once_with("What are AWS best practices?", k=5)


# Pipeline.ask() — with reranker 

class TestAskWithReranker:

    def test_ask_with_reranker_calls_rerank(self, pipeline_with_reranker, mock_reranker):
        pipeline_with_reranker.ask("What are AWS best practices?", k=3)
        mock_reranker.rerank.assert_called_once()

    def test_ask_with_reranker_retrieves_2k_candidates(self, pipeline_with_reranker, mock_retriever):
        pipeline_with_reranker.ask("What are AWS best practices?", k=3)
        mock_retriever.retrieve.assert_called_once_with("What are AWS best practices?", k=6)

    def test_ask_without_reranker_skips_rerank(self, pipeline, mock_reranker):
        pipeline.ask("What are AWS best practices?", k=3)
        mock_reranker.rerank.assert_not_called()

    def test_ask_without_reranker_retrieves_exact_k(self, pipeline, mock_retriever):
        pipeline.ask("What are AWS best practices?", k=3)
        mock_retriever.retrieve.assert_called_once_with("What are AWS best practices?", k=3)


# Pipeline.ask() — CRAG 

class TestCRAG:

    def test_crag_returns_fallback_when_not_relevant(self, mock_loader, mock_cleaner, mock_splitter, mock_embedder, mock_vectorstore, mock_retriever, mock_generator, mock_reranker, sample_chunks):
        # Reranker returns low scores → not relevant
        mock_reranker.rerank.return_value = [
            Document(
                content=sample_chunks[0].content,
                metadata={**sample_chunks[0].metadata, "rerank_score": -5.0}
            )
        ]
        pipeline = Pipeline(
            loaders=[mock_loader],
            cleaner=mock_cleaner,
            splitter=mock_splitter,
            embedder=mock_embedder,
            vectorstore=mock_vectorstore,
            retriever=mock_retriever,
            generator=mock_generator,
            reranker=mock_reranker,
            relevance_threshold=0.0
        )
        response = pipeline.ask("What are AWS best practices?", k=3)
        assert "I don't have enough information" in response
        mock_generator.generate.assert_not_called()

    def test_crag_generates_when_relevant(self, mock_loader, mock_cleaner, mock_splitter, mock_embedder, mock_vectorstore, mock_retriever, mock_generator, mock_reranker, sample_chunks):
        # Reranker returns high scores → relevant
        mock_reranker.rerank.return_value = [
            Document(
                content=sample_chunks[0].content,
                metadata={**sample_chunks[0].metadata, "rerank_score": 5.0}
            )
        ]
        pipeline = Pipeline(
            loaders=[mock_loader],
            cleaner=mock_cleaner,
            splitter=mock_splitter,
            embedder=mock_embedder,
            vectorstore=mock_vectorstore,
            retriever=mock_retriever,
            generator=mock_generator,
            reranker=mock_reranker,
            relevance_threshold=0.0
        )
        response = pipeline.ask("What are AWS best practices?", k=3)
        mock_generator.generate.assert_called_once()

    def test_crag_disabled_when_no_threshold(self, pipeline_with_reranker, mock_generator, mock_reranker, sample_chunks):
        mock_reranker.rerank.return_value = [
            Document(
                content=sample_chunks[0].content,
                metadata={**sample_chunks[0].metadata, "rerank_score": -5.0}
            )
        ]
        pipeline_with_reranker.ask("What are AWS best practices?", k=3)
        # No threshold set → CRAG disabled → generator always called
        mock_generator.generate.assert_called_once()

    def test_crag_disabled_when_no_reranker(self, pipeline, mock_generator):
        # No reranker → CRAG impossible → generator always called
        pipeline.ask("What are AWS best practices?", k=3)
        mock_generator.generate.assert_called_once()