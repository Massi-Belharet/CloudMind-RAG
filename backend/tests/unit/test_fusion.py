"""
Tests for fusion module 

Covers rrf_fusion() with two ranked lists (Hybrid Search case),
N ranked lists (Multi-Query case), weighting, deduplication and edge cases.
"""

import pytest

from src.loaders.base_loader import Document
from src.rag.fusion import rrf_fusion


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


# rrf_fusion() — two lists (Hybrid Search case)

class TestRRFFusionTwoLists:

    def test_returns_k_results(self, sample_documents):
        list_a = [sample_documents[0], sample_documents[1]]
        list_b = [sample_documents[1], sample_documents[2]]

        fused = rrf_fusion([list_a, list_b], k=2)
        assert len(fused) == 2

    def test_prioritizes_documents_in_both_lists(self, sample_documents):
        list_a = [sample_documents[0], sample_documents[1]]
        list_b = [sample_documents[1], sample_documents[2]]

        fused = rrf_fusion([list_a, list_b], k=1)
        # sample_documents[1] appears in both lists → should rank first
        assert fused[0].content == sample_documents[1].content

    def test_no_duplicates(self, sample_documents):
        list_a = [sample_documents[0], sample_documents[1]]
        list_b = [sample_documents[0], sample_documents[1]]

        fused = rrf_fusion([list_a, list_b], k=5)
        contents = [doc.content for doc in fused]
        assert len(contents) == len(set(contents))

    def test_respects_weights(self, sample_documents):
        list_a = [sample_documents[0]]
        list_b = [sample_documents[1]]

        # Heavily weight list_b → its document should rank first
        fused = rrf_fusion([list_a, list_b], weights=[0.1, 0.9], k=2)
        assert fused[0].content == sample_documents[1].content


# rrf_fusion() — N lists (Multi-Query case)

class TestRRFFusionMultipleLists:

    def test_fuses_three_lists(self, sample_documents):
        list_a = [sample_documents[0], sample_documents[1]]
        list_b = [sample_documents[1], sample_documents[2]]
        list_c = [sample_documents[1], sample_documents[3]]

        fused = rrf_fusion([list_a, list_b, list_c], k=4)
        assert len(fused) == 4

    def test_document_in_all_lists_ranks_first(self, sample_documents):
        list_a = [sample_documents[0], sample_documents[1]]
        list_b = [sample_documents[1], sample_documents[2]]
        list_c = [sample_documents[1], sample_documents[3]]

        # sample_documents[1] appears in all 3 lists → should rank first
        fused = rrf_fusion([list_a, list_b, list_c], k=1)
        assert fused[0].content == sample_documents[1].content

    def test_default_weights_are_equal(self, sample_documents):
        list_a = [sample_documents[0]]
        list_b = [sample_documents[1]]
        list_c = [sample_documents[2]]

        fused = rrf_fusion([list_a, list_b, list_c], k=3)
        assert len(fused) == 3


# rrf_fusion() — edge cases 

class TestRRFFusionEdgeCases:

    def test_empty_lists_returns_empty(self):
        fused = rrf_fusion([[], []], k=5)
        assert fused == []

    def test_single_list(self, sample_documents):
        fused = rrf_fusion([sample_documents[:3]], k=2)
        assert len(fused) == 2
        assert fused[0].content == sample_documents[0].content

    def test_custom_rrf_k(self, sample_documents):
        list_a = [sample_documents[0]]
        list_b = [sample_documents[1]]

        fused_default = rrf_fusion([list_a, list_b], k=2, rrf_k=60)
        fused_custom = rrf_fusion([list_a, list_b], k=2, rrf_k=1)

        assert len(fused_default) == 2
        assert len(fused_custom) == 2