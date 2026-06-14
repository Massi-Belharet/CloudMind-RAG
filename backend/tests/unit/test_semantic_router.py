"""
Tests for SemanticRouter module 

Covers route embedding initialization, cosine similarity computation,
and routing logic with threshold-based provider detection.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock

from src.embeddings.base_embeddings import BaseEmbedder
from src.rag.semantic_router import SemanticRouter, ROUTE_DESCRIPTIONS


# Fixtures 

@pytest.fixture
def mock_embedder():
    embedder = MagicMock(spec=BaseEmbedder)

    def embed_query_side_effect(text: str) -> np.ndarray:
        # Return deterministic vectors based on content
        if "aws" in text.lower() or "amazon" in text.lower() or "ec2" in text.lower():
            vec = np.array([1.0, 0.0, 0.0, 0.0])
        elif "azure" in text.lower() or "microsoft" in text.lower():
            vec = np.array([0.0, 1.0, 0.0, 0.0])
        elif "gcp" in text.lower() or "google" in text.lower():
            vec = np.array([0.0, 0.0, 1.0, 0.0])
        elif "rgpd" in text.lower() or "compliance" in text.lower() or "gdpr" in text.lower():
            vec = np.array([0.0, 0.0, 0.0, 1.0])
        else:
            vec = np.array([0.25, 0.25, 0.25, 0.25])
        return vec / np.linalg.norm(vec)

    embedder.embed_query.side_effect = embed_query_side_effect
    return embedder


@pytest.fixture
def router(mock_embedder):
    return SemanticRouter(embedder=mock_embedder, threshold=0.75)


# SemanticRouter.__init__() 

class TestInit:

    def test_builds_route_embeddings_for_all_providers(self, router):
        assert set(router.route_embeddings.keys()) == set(ROUTE_DESCRIPTIONS.keys())

    def test_route_embeddings_are_numpy_arrays(self, router):
        for vec in router.route_embeddings.values():
            assert isinstance(vec, np.ndarray)

    def test_embedder_called_for_each_provider(self, mock_embedder):
        SemanticRouter(embedder=mock_embedder, threshold=0.75)
        assert mock_embedder.embed_query.call_count == len(ROUTE_DESCRIPTIONS)


# SemanticRouter._cosine_similarity()

class TestCosineSimilarity:

    def test_identical_vectors_return_1(self, router):
        vec = np.array([1.0, 0.0, 0.0, 0.0])
        assert round(router._cosine_similarity(vec, vec), 5) == 1.0

    def test_orthogonal_vectors_return_0(self, router):
        vec_a = np.array([1.0, 0.0, 0.0, 0.0])
        vec_b = np.array([0.0, 1.0, 0.0, 0.0])
        assert round(router._cosine_similarity(vec_a, vec_b), 5) == 0.0

    def test_returns_float(self, router):
        vec = np.array([1.0, 0.0, 0.0, 0.0])
        result = router._cosine_similarity(vec, vec)
        assert isinstance(result, float)


# SemanticRouter.route()

class TestRoute:

    def test_routes_aws_query(self, router):
        result = router.route("How to reduce AWS EC2 costs?")
        assert result == "aws"

    def test_routes_azure_query(self, router):
        result = router.route("Azure Microsoft virtual machine pricing")
        assert result == "azure"

    def test_routes_gcp_query(self, router):
        result = router.route("GCP Google Cloud BigQuery pricing")
        assert result == "gcp"

    def test_routes_compliance_query(self, router):
        result = router.route("RGPD GDPR compliance data residency")
        assert result == "compliance"

    def test_returns_none_for_ambiguous_query(self, router):
        result = router.route("general cloud optimization strategy")
        assert result is None

    def test_returns_none_below_threshold(self, mock_embedder):
        router = SemanticRouter(embedder=mock_embedder, threshold=0.99)
        result = router.route("general cloud optimization strategy")
        assert result is None

    def test_returns_string_when_above_threshold(self, router):
        result = router.route("AWS EC2 cost optimization")
        assert isinstance(result, str)