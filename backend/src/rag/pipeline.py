"""
RAG Pipeline module

Orchestrates the full RAG pipeline by assembling all components:
loaders, cleaner, splitter, embedder, vector store, retriever, and generator.
Exposes two simple methods — build() to index documents and ask() to query them.

Functions:
    build() -> None : Load, clean, split, embed and index all documents.
    ask(query: str, k: int) -> str : Retrieve relevant chunks and generate a response.
    ask_stream(query: str, k: int) -> Iterator[str] : Retrieve relevant chunks and stream a response.
"""

from typing import Iterator, List, Optional
import numpy as np

from src.loaders.base_loader import BaseLoader, Document
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.base_embeddings import BaseEmbedder
from src.vectorstores.base_vectorstore import BaseVectorStore, PersistableStore
from src.rag.retriever import Retriever
from src.rag.reranker import Reranker
from src.rag.semantic_router import SemanticRouter
from src.llm.base import BaseLLM
from langsmith import traceable


class Pipeline:

    def __init__(self, loaders: List[BaseLoader], cleaner: TextCleaner, splitter: TextSplitter, embedder: BaseEmbedder, vectorstore: BaseVectorStore, retriever: Retriever, generator: BaseLLM, reranker: Optional[Reranker] = None, relevance_threshold: Optional[float] = None, router: Optional[SemanticRouter] = None, storage_path: str = "backend/data/processed/faiss"):
        """
        Initialize the RAG pipeline with all required components.

        Args:
            loaders (List[BaseLoader]): List of document loaders (PDF, Markdown, CSV).
            cleaner (TextCleaner): Text cleaner instance.
            splitter (TextSplitter): Text splitter instance.
            embedder (BaseEmbedder): Embedder instance to encode chunks.
            vectorstore (BaseVectorStore): Vector store instance to index chunks.
            retriever (Retriever): Retriever instance to search relevant chunks.
            generator (BaseLLM): Generator instance to produce responses.
            reranker (Optional[Reranker]): Optional reranker to improve retrieval quality. Defaults to None.
            relevance_threshold (Optional[float]): CRAG relevance threshold. If set, enables CRAG evaluation. Defaults to None.
            router (Optional[SemanticRouter]): Optional semantic router. If set, routes the
                original query to a provider once per call and restricts retrieval to it.
                Defaults to None, which searches across all providers (unchanged behavior).
            storage_path (str): Path to persist the vector store. Defaults to backend/data/processed/faiss.
        """
        self.loaders = loaders
        self.cleaner = cleaner
        self.splitter = splitter
        self.embedder = embedder
        self.vectorstore = vectorstore
        self.retriever = retriever
        self.generator = generator
        self.reranker = reranker
        self.relevance_threshold = relevance_threshold
        self.router = router
        self.storage_path = storage_path

    def build(self) -> None:
        """
        Load, clean, split, embed and index all documents into the vector store.
        Persists the vector store to disk only if the store supports persistence.
        """
        # Load all documents
        documents = []
        for loader in self.loaders:
            documents.extend(loader.load())
        print(f"Loaded {len(documents)} documents")

        # Clean documents
        documents = self.cleaner.clean(documents)
        print(f"Cleaned {len(documents)} documents")

        # Split into chunks
        chunks = self.splitter.split(documents)
        print(f"Split into {len(chunks)} chunks")

        # Embed chunks
        vectors = self.embedder.embed(chunks)
        print(f"Embedded {len(chunks)} chunks")

        # Index into vector store
        self.vectorstore.add(chunks, vectors)
        print(f"Indexed {len(chunks)} chunks")

        # Persist to disk only if store supports it
        if isinstance(self.vectorstore, PersistableStore):
            self.vectorstore.save(self.storage_path)
            print(f"Vector store saved to {self.storage_path}")

    def _is_relevant(self, query: str, documents: List[Document]) -> bool:
        """
        Evaluate whether retrieved documents are relevant to the query using reranker scores.

        Args:
            query (str): User question.
            documents (List[Document]): Retrieved documents to evaluate.

        Returns:
            bool: True if average rerank score meets the relevance threshold.
        """
        if not documents:
            return False

        scored = self.reranker.rerank(query, documents, top_k=len(documents))
        scores = [doc.metadata.get("rerank_score", 0.0) for doc in scored]
        return float(np.mean(scores)) >= self.relevance_threshold


    @traceable(name="CloudMind-RAG-Pipeline")
    def ask(self, query: str, k: int = 5) -> str:
        """
        Retrieve relevant chunks and generate a response to the query.
        If a reranker is configured, retrieves 2*k candidates and reranks them.
        If relevance_threshold is set, enables CRAG evaluation before generation.
        If a router is configured, routes the original query to a provider once
        and restricts retrieval (original query and all reformulations) to it.

        Args:
            query (str): User question to answer.
            k (int): Number of chunks to retrieve. Defaults to 5.

        Returns:
            str: Generated response from the LLM.
        """
        # Route once on the original query — never re-detected per reformulation
        filter_provider = self.router.route(query) if self.router else None

        # Retrieve more candidates if reranking afterwards
        retrieve_k = k * 2 if self.reranker else k
        documents = self.retriever.retrieve(query, k=retrieve_k, filter_provider=filter_provider)
        print(f"Retrieved {len(documents)} chunks")

        # Rerank if configured
        if self.reranker:
            documents = self.reranker.rerank(query, documents, top_k=k)
            print(f"Reranked to {len(documents)} chunks")

        # CRAG to evaluate relevance if threshold is set
        if self.reranker and self.relevance_threshold is not None:
            if not self._is_relevant(query, documents):
                return "I don't have enough information in my knowledge base to answer this question."

        # Generate response
        response = self.generator.generate(query, documents)

        return response

    @traceable(name="CloudMind-RAG-Pipeline-Stream")
    def ask_stream(self, query: str, k: int = 5) -> Iterator[str]:
        """
        Retrieve relevant chunks and stream a response to the query as it is
        generated. Mirrors ask()'s retrieval, reranking, routing and CRAG logic
        exactly, but yields text fragments from the generator's streaming method
        instead of waiting for the full response. If CRAG determines the retrieved
        documents are not relevant, yields the same static fallback message as
        ask() as a single-item stream, without calling the LLM.

        Args:
            query (str): User question to answer.
            k (int): Number of chunks to retrieve. Defaults to 5.

        Yields:
            str: Successive text fragments of the generated response.
        """
        # Route once on the original query — never re-detected per reformulation
        filter_provider = self.router.route(query) if self.router else None

        # Retrieve more candidates if reranking afterwards
        retrieve_k = k * 2 if self.reranker else k
        documents = self.retriever.retrieve(query, k=retrieve_k, filter_provider=filter_provider)
        print(f"Retrieved {len(documents)} chunks")

        # Rerank if configured
        if self.reranker:
            documents = self.reranker.rerank(query, documents, top_k=k)
            print(f"Reranked to {len(documents)} chunks")

        # CRAG to evaluate relevance if threshold is set — same protective
        # short-circuit as ask(), yielded as a single-item stream instead of
        # calling the LLM.
        if self.reranker and self.relevance_threshold is not None:
            if not self._is_relevant(query, documents):
                yield "I don't have enough information in my knowledge base to answer this question."
                return

        # Stream the generated response
        yield from self.generator.generate_stream(query, documents)