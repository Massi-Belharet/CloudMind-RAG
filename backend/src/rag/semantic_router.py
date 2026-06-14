"""
Semantic Router module 

Routes user queries to the most relevant cloud provider namespace
using embedding-based cosine similarity. Each provider has a reference
embedding computed from representative keywords at initialization.
If no provider exceeds the confidence threshold, routing falls back
to searching across all providers.

Functions:
    route(query: str) -> Optional[str] : Return the best matching provider or None if below threshold.
"""

from typing import Optional
import numpy as np

from src.embeddings.base_embeddings import BaseEmbedder


# Reference descriptions per provider (used to build route embeddings)
ROUTE_DESCRIPTIONS = {
    "aws": "AWS Amazon Web Services EC2 S3 Lambda RDS CloudFront IAM cost optimization billing",
    "azure": "Azure Microsoft cloud virtual machines blob storage cost management resource groups",
    "gcp": "GCP Google Cloud Platform BigQuery Cloud Run Kubernetes Engine billing export",
    "compliance": "RGPD GDPR compliance data residency EU regulation personal data processing",
}


class SemanticRouter:

    def __init__(self, embedder: BaseEmbedder, threshold: float = 0.75):
        """
        Initialize SemanticRouter and pre-compute route embeddings.

        Args:
            embedder (BaseEmbedder): Embedder instance used to encode queries and route descriptions.
            threshold (float): Minimum cosine similarity score to commit to a route. Defaults to 0.75.
        """
        self.embedder = embedder
        self.threshold = threshold
        self.route_embeddings = self._build_route_embeddings()

    def _build_route_embeddings(self) -> dict:
        """
        Pre-compute embeddings for each route description.

        Returns:
            dict: Mapping from provider name to its reference embedding vector.
        """
        return {
            provider: self.embedder.embed_query(description)
            for provider, description in ROUTE_DESCRIPTIONS.items()
        }

    def _cosine_similarity(self, vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """
        Compute cosine similarity between two vectors.

        Args:
            vec_a (np.ndarray): First vector.
            vec_b (np.ndarray): Second vector.

        Returns:
            float: Cosine similarity score between 0 and 1.
        """
        return float(np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b)))

    def route(self, query: str) -> Optional[str]:
        """
        Route the query to the most relevant cloud provider namespace.

        Computes cosine similarity between the query embedding and each
        provider's reference embedding. Returns the best matching provider
        if its score exceeds the threshold, otherwise returns None to signal
        that all providers should be searched.

        Args:
            query (str): User question to route.

        Returns:
            Optional[str]: Provider name (aws, azure, gcp, compliance) or None if below threshold.
        """
        query_vector = self.embedder.embed_query(query)

        best_provider = None
        best_score = -1.0

        for provider, route_vector in self.route_embeddings.items():
            score = self._cosine_similarity(query_vector, route_vector)
            if score > best_score:
                best_score = score
                best_provider = provider

        if best_score >= self.threshold:
            return best_provider

        return None