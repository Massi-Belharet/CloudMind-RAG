"""
Tests for Embedder module 

"""

import pytest
import numpy as np
from src.loaders.base_loader import Document
from src.embeddings.embedder import Embedder


#  Fixtures 

@pytest.fixture(scope="module")
def embedder():

    # we use lightweight model for tests

    return Embedder(model_name="all-MiniLM-L6-v2")


@pytest.fixture
def sample_documents():
    return [
        Document(
            content="AWS recommends using multiple availability zones.",
            metadata={"file_type": "pdf", "provider": "aws"}
        ),
        Document(
            content="Cost optimization is a key pillar of cloud architecture.",
            metadata={"file_type": "pdf", "provider": "aws"}
        ),
        Document(
            content="Azure hybrid cloud enables seamless integration.",
            metadata={"file_type": "markdown", "provider": "azure"}
        )
    ]


@pytest.fixture
def single_document():
    return [Document(
        content="GCP recommends using Cloud Run for serverless workloads.",
        metadata={"file_type": "markdown", "provider": "gcp"}
    )]


# Embedder.embed() 

class TestEmbed:

    def test_embed_returns_numpy_array(self, embedder, sample_documents):
        vectors = embedder.embed(sample_documents)
        assert isinstance(vectors, np.ndarray)

    def test_embed_correct_shape(self, embedder, sample_documents):
        vectors = embedder.embed(sample_documents)
        assert vectors.shape[0] == len(sample_documents)
        assert vectors.shape[1] > 0

    def test_embed_single_document(self, embedder, single_document):
        vectors = embedder.embed(single_document)
        assert vectors.shape[0] == 1

    def test_embed_vectors_are_not_zero(self, embedder, sample_documents):
        vectors = embedder.embed(sample_documents)
        assert not np.all(vectors == 0)

    def test_embed_different_docs_different_vectors(self, embedder, sample_documents):
        vectors = embedder.embed(sample_documents)
        assert not np.allclose(vectors[0], vectors[1])


#  Embedder.embed_query() 

class TestEmbedQuery:

    def test_embed_query_returns_numpy_array(self, embedder):
        vector = embedder.embed_query("What are the FinOps best practices?")
        assert isinstance(vector, np.ndarray)

    def test_embed_query_returns_1d_vector(self, embedder):
        vector = embedder.embed_query("What are the FinOps best practices?")
        assert vector.ndim == 1

    def test_embed_query_correct_dimension(self, embedder, sample_documents):
        doc_vectors = embedder.embed(sample_documents)
        query_vector = embedder.embed_query("What are the FinOps best practices?")
        assert query_vector.shape[0] == doc_vectors.shape[1]

    def test_embed_query_not_zero(self, embedder):
        vector = embedder.embed_query("What are the FinOps best practices?")
        assert not np.all(vector == 0)