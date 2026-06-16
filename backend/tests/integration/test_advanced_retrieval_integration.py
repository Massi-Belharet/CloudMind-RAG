"""
Integration tests for Advanced RAG components in CloudMind pipeline.

Tests HybridRetriever, Reranker, SemanticRouter, MultiQueryRetriever
and the full Pipeline.ask() end-to-end with real models and infrastructure.

Requires:
    - Docker running (Qdrant on localhost:6333)
    - Ollama running (qwen3.5:9b and qwen3.5:2b on localhost:11434)
    - nomic-embed-text-v1.5 and bge-reranker-v2-m3 downloaded
"""

import pytest
from langchain_ollama import ChatOllama
from qdrant_client import QdrantClient

from src.loaders.base_loader import Document
from src.embeddings.embedder import Embedder
from src.vectorstores.qdrant_store import QdrantStore
from src.rag.retriever import Retriever
from src.rag.hybrid_retriever import HybridRetriever
from src.rag.reranker import Reranker
from src.rag.semantic_router import SemanticRouter
from src.rag.multi_query_retriever import MultiQueryRetriever
from src.rag.pipeline import Pipeline
from src.llm.generator import Generator
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.utils.config import config
from src.utils.settings import settings


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def embedder():
    return Embedder(model_name=config.embedding.model)


@pytest.fixture(scope="module")
def sample_documents():
    return [
        Document(
            content="AWS EC2 t3.medium costs 0.0416 dollars per hour in us-east-1 region.",
            metadata={"provider": "aws", "file_type": "csv"}
        ),
        Document(
            content="AWS recommends using reserved instances for cost optimization on EC2.",
            metadata={"provider": "aws", "file_type": "pdf"}
        ),
        Document(
            content="Azure virtual machines B2s costs 0.0416 dollars per hour in West Europe.",
            metadata={"provider": "azure", "file_type": "csv"}
        ),
        Document(
            content="Azure cost management best practices include using spending limits and budgets.",
            metadata={"provider": "azure", "file_type": "pdf"}
        ),
        Document(
            content="GCP Cloud Run is a serverless platform that charges per request.",
            metadata={"provider": "gcp", "file_type": "markdown"}
        ),
        Document(
            content="RGPD article 28 requires data processing agreements with all cloud subprocessors.",
            metadata={"provider": "compliance", "file_type": "pdf"}
        ),
    ]


@pytest.fixture(scope="module")
def vectors(embedder, sample_documents):
    return embedder.embed(sample_documents)


@pytest.fixture(scope="module")
def qdrant_store(vectors, sample_documents):
    store = QdrantStore(
        collection_name="test_advanced_retrieval_integration",
        embedding_dim=config.embedding.dim
    )
    store.add(sample_documents, vectors)
    return store


@pytest.fixture(scope="module")
def retriever(embedder, qdrant_store):
    return Retriever(embedder=embedder, vectorstore=qdrant_store)


@pytest.fixture(scope="module")
def llm():
    return ChatOllama(
        model=config.llm.model,
        base_url=f"http://{settings.ollama_host}:{settings.ollama_port}"
    )


@pytest.fixture(scope="module")
def llm_multi_query():
    return ChatOllama(
        model=config.llm.multi_query_model,
        base_url=f"http://{settings.ollama_host}:{settings.ollama_port}",
        think=False
    )


@pytest.fixture(scope="module")
def generator(llm):
    return Generator(llm=llm)


@pytest.fixture(scope="module")
def pipeline(embedder, qdrant_store, retriever, generator):
    return Pipeline(
        loaders=[],
        cleaner=TextCleaner(),
        splitter=TextSplitter(
            chunk_size=config.rag.chunk_size,
            chunk_overlap=config.rag.chunk_overlap
        ),
        embedder=embedder,
        vectorstore=qdrant_store,
        retriever=retriever,
        generator=generator,
        reranker=Reranker()
    )


@pytest.fixture(scope="module", autouse=True)
def cleanup_qdrant():
    yield
    client = QdrantClient(host="localhost", port=6333)
    if client.collection_exists("test_advanced_retrieval_integration"):
        client.delete_collection("test_advanced_retrieval_integration")
        print("✅ Collection 'test_advanced_retrieval_integration' deleted")


# ── HybridRetriever Integration ───────────────────────────────────────────────

@pytest.mark.integration
class TestHybridRetrieverIntegration:

    def test_hybrid_retrieve_returns_documents(self, retriever, sample_documents):
        hybrid = HybridRetriever(retriever=retriever, documents=sample_documents)
        results = hybrid.retrieve("AWS EC2 cost optimization", k=3)
        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)

    def test_hybrid_retrieve_relevant_to_query(self, retriever, sample_documents):
        hybrid = HybridRetriever(retriever=retriever, documents=sample_documents)
        results = hybrid.retrieve("AWS EC2 t3.medium pricing", k=2)
        providers = [r.metadata.get("provider") for r in results]
        assert "aws" in providers


# ── Reranker Integration ──────────────────────────────────────────────────────

@pytest.mark.integration
class TestRerankerIntegration:

    def test_reranker_returns_documents_with_scores(self, sample_documents):
        reranker = Reranker()
        results = reranker.rerank(
            "AWS cost optimization best practices",
            sample_documents,
            top_k=3
        )
        assert len(results) == 3
        for doc in results:
            assert "rerank_score" in doc.metadata

    def test_reranker_orders_by_relevance(self, sample_documents):
        reranker = Reranker()
        results = reranker.rerank(
            "AWS EC2 t3.medium cost per hour",
            sample_documents,
            top_k=3
        )
        scores = [doc.metadata["rerank_score"] for doc in results]
        assert scores == sorted(scores, reverse=True)


# ── SemanticRouter Integration ────────────────────────────────────────────────

@pytest.mark.integration
class TestSemanticRouterIntegration:

    def test_routes_aws_query(self, embedder):
        router = SemanticRouter(embedder=embedder)
        result = router.route("How to reduce AWS EC2 costs with reserved instances?")
        assert result == "aws"

    def test_routes_azure_query(self, embedder):
        router = SemanticRouter(embedder=embedder)
        result = router.route("Azure virtual machine pricing and cost management")
        assert result == "azure"

    def test_routes_compliance_query(self, embedder):
        router = SemanticRouter(embedder=embedder)
        result = router.route("RGPD data processing agreements cloud providers")
        assert result == "compliance"

    def test_returns_none_for_general_query(self, embedder):
        router = SemanticRouter(embedder=embedder, threshold=0.99)
        result = router.route("How to optimize my infrastructure?")
        assert result is None


# ── MultiQueryRetriever Integration ──────────────────────────────────────────

@pytest.mark.integration
class TestMultiQueryRetrieverIntegration:

    def test_generates_reformulations(self, llm_multi_query, retriever, sample_documents):
        hybrid = HybridRetriever(retriever=retriever, documents=sample_documents)
        mq = MultiQueryRetriever(llm=llm_multi_query, retriever=hybrid, n_queries=3)
        reformulations = mq._generate_queries("How to reduce cloud costs?")
        assert len(reformulations) > 0
        assert all(isinstance(q, str) for q in reformulations)

    def test_reformulations_are_non_empty(self, llm_multi_query, retriever, sample_documents):
        hybrid = HybridRetriever(retriever=retriever, documents=sample_documents)
        mq = MultiQueryRetriever(llm=llm_multi_query, retriever=hybrid, n_queries=3)
        reformulations = mq._generate_queries("How to reduce cloud costs?")
        assert all(len(q.strip()) > 0 for q in reformulations)

    def test_retrieve_returns_documents(self, llm_multi_query, retriever, sample_documents):
        hybrid = HybridRetriever(retriever=retriever, documents=sample_documents)
        mq = MultiQueryRetriever(llm=llm_multi_query, retriever=hybrid, n_queries=3)
        results = mq.retrieve("How to reduce cloud costs?", k=3)
        assert len(results) == 3
        assert all(isinstance(r, Document) for r in results)


# ── Pipeline End-to-End ───────────────────────────────────────────────────────

@pytest.mark.integration
class TestPipelineEndToEnd:

    def test_ask_returns_string(self, pipeline):
        response = pipeline.ask("What are AWS cost optimization best practices?", k=3)
        assert isinstance(response, str)

    def test_ask_returns_non_empty_response(self, pipeline):
        response = pipeline.ask("What are AWS cost optimization best practices?", k=3)
        assert len(response.strip()) > 0

    def test_ask_with_crag_relevant_query(self, embedder, qdrant_store, retriever, generator):
        pipeline_crag = Pipeline(
            loaders=[],
            cleaner=TextCleaner(),
            splitter=TextSplitter(
                chunk_size=config.rag.chunk_size,
                chunk_overlap=config.rag.chunk_overlap
            ),
            embedder=embedder,
            vectorstore=qdrant_store,
            retriever=retriever,
            generator=generator,
            reranker=Reranker(),
            relevance_threshold=config.rag.relevance_threshold
        )
        response = pipeline_crag.ask("What are AWS EC2 reserved instances?", k=3)
        assert isinstance(response, str)

    def test_ask_with_crag_irrelevant_query(self, embedder, qdrant_store, retriever, generator):
        pipeline_crag = Pipeline(
            loaders=[],
            cleaner=TextCleaner(),
            splitter=TextSplitter(
                chunk_size=config.rag.chunk_size,
                chunk_overlap=config.rag.chunk_overlap
            ),
            embedder=embedder,
            vectorstore=qdrant_store,
            retriever=retriever,
            generator=generator,
            reranker=Reranker(),
            relevance_threshold=100.0
        )
        response = pipeline_crag.ask("What is the price of a Tesla Model S?", k=3)
        assert "I don't have enough information" in response