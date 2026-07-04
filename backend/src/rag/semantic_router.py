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


# Reference descriptions per provider (used to build route embeddings).
# Written as natural-language sentences rather than keyword lists: short
# keyword strings under-discriminate against real user questions once
# embedded with bge-m3 (see backend/scripts/calibrate_router_threshold.py).
ROUTE_DESCRIPTIONS = {
    "aws": (
        "Questions about Amazon Web Services (AWS) cloud infrastructure and services, "
        "such as EC2 virtual machines, S3 storage, Lambda serverless functions, RDS "
        "databases, CloudFront CDN, and IAM access management, including the AWS "
        "Well-Architected Framework and AWS-specific cost optimization and billing."
    ),
    "azure": (
        "Questions about Microsoft Azure cloud infrastructure and services, such as "
        "Azure virtual machines, Blob Storage, Azure Active Directory, and resource "
        "groups, including the Azure Well-Architected Framework and Azure-specific "
        "cost management, reserved instances, and billing."
    ),
    "gcp": (
        "Questions about Google Cloud Platform (GCP) infrastructure and services, "
        "such as BigQuery, Cloud Run, Google Kubernetes Engine, and Cloud Storage, "
        "including the Google Cloud Architecture Framework and GCP-specific cost "
        "optimization, billing export, and sustainability."
    ),
    "compliance": (
        "Questions about regulatory and legal compliance for cloud workloads, such "
        "as RGPD or GDPR data protection requirements, data residency, EU "
        "regulations on personal data processing, and the EU Cloud Code of Conduct."
    ),
}


class SemanticRouter:

    def __init__(self, embedder: BaseEmbedder, threshold: float = 0.60):
        """
        Initialize SemanticRouter and pre-compute route embeddings.

        Args:
            embedder (BaseEmbedder): Embedder instance used to encode queries and route descriptions.
            threshold (float): Minimum cosine similarity score to commit to a route. Defaults to 0.60.
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