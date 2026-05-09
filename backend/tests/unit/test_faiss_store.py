"""
Tests for FAISSStore module 

"""

import os
import pytest
import numpy as np
from src.loaders.base_loader import Document
from src.vectorstores.faiss_store import FAISSStore


# Fixtures

@pytest.fixture
def embedding_dim():
    return 384


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
        ),
        Document(
            content="GCP recommends Cloud Run for serverless workloads.",
            metadata={"file_type": "markdown", "provider": "gcp"}
        ),
        Document(
            content="RGPD requires data residency compliance in Europe.",
            metadata={"file_type": "pdf", "provider": "compliance"}
        )
    ]


@pytest.fixture
def sample_vectors(embedding_dim):
    np.random.seed(42)
    return np.random.rand(5, embedding_dim).astype("float32")


@pytest.fixture
def query_vector(embedding_dim):
    np.random.seed(99)
    return np.random.rand(embedding_dim).astype("float32")


@pytest.fixture
def store(embedding_dim, sample_documents, sample_vectors):
    s = FAISSStore(collection_name="test_collection", embedding_dim=embedding_dim)
    s.add(sample_documents, sample_vectors)
    return s


@pytest.fixture
def tmp_storage_path(tmp_path):
    return str(tmp_path / "faiss_store")


# FAISSStore.add() 

class TestAdd:

    def test_add_stores_documents(self, store, sample_documents):
        assert len(store.documents) == len(sample_documents)

    def test_add_indexes_vectors(self, store, sample_documents):
        assert store.index.ntotal == len(sample_documents)

    def test_add_multiple_batches(self, embedding_dim):
        store = FAISSStore(collection_name="test", embedding_dim=embedding_dim)
        docs1 = [Document(content="Doc 1", metadata={"file_type": "pdf", "provider": "aws"})]
        docs2 = [Document(content="Doc 2", metadata={"file_type": "pdf", "provider": "azure"})]
        vecs1 = np.random.rand(1, embedding_dim).astype("float32")
        vecs2 = np.random.rand(1, embedding_dim).astype("float32")
        store.add(docs1, vecs1)
        store.add(docs2, vecs2)
        assert store.index.ntotal == 2
        assert len(store.documents) == 2


# FAISSStore.search()
class TestSearch:

    def test_search_returns_documents(self, store, query_vector):
        results = store.search(query_vector, k=3)
        assert len(results) > 0
        assert all(isinstance(r, Document) for r in results)

    def test_search_returns_k_results(self, store, query_vector):
        results = store.search(query_vector, k=3)
        assert len(results) == 3

    def test_search_results_have_similarity_score(self, store, query_vector):
        results = store.search(query_vector, k=3)
        for result in results:
            assert "similarity_score" in result.metadata

    def test_search_similarity_score_between_0_and_1(self, store, query_vector):
        results = store.search(query_vector, k=3)
        for result in results:
            assert 0.0 <= result.metadata["similarity_score"] <= 1.0

    def test_search_preserves_metadata(self, store, query_vector):
        results = store.search(query_vector, k=3)
        for result in results:
            assert "provider" in result.metadata
            assert "file_type" in result.metadata

    def test_search_k_greater_than_total(self, store, query_vector):
        results = store.search(query_vector, k=10)
        assert len(results) <= 5


#  FAISSStore.save() + load() 

class TestSaveLoad:

    def test_save_creates_files(self, store, tmp_storage_path):
        store.save(tmp_storage_path)
        assert os.path.exists(os.path.join(tmp_storage_path, "test_collection.index"))
        assert os.path.exists(os.path.join(tmp_storage_path, "test_collection.json"))

    def test_load_restores_documents(self, store, tmp_storage_path, embedding_dim):
        store.save(tmp_storage_path)
        new_store = FAISSStore(collection_name="test_collection", embedding_dim=embedding_dim)
        new_store.load(tmp_storage_path)
        assert len(new_store.documents) == len(store.documents)

    def test_load_restores_index(self, store, tmp_storage_path, embedding_dim):
        store.save(tmp_storage_path)
        new_store = FAISSStore(collection_name="test_collection", embedding_dim=embedding_dim)
        new_store.load(tmp_storage_path)
        assert new_store.index.ntotal == store.index.ntotal

    def test_load_search_returns_same_results(self, store, tmp_storage_path, embedding_dim, query_vector):
        store.save(tmp_storage_path)
        new_store = FAISSStore(collection_name="test_collection", embedding_dim=embedding_dim)
        new_store.load(tmp_storage_path)
        results = new_store.search(query_vector, k=3)
        assert len(results) == 3

    def test_load_raises_error_if_not_found(self, embedding_dim):
        store = FAISSStore(collection_name="test_collection", embedding_dim=embedding_dim)
        with pytest.raises(FileNotFoundError):
            store.load("non_existent_path")