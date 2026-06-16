"""
RAG Pipeline module 

Orchestrates the full RAG pipeline by assembling all components:
loaders, cleaner, splitter, embedder, vector store, retriever, and generator.
Exposes two simple methods — build() to index documents and ask() to query them.

Functions:
    build() -> None : Load, clean, split, embed and index all documents.
    ask(query: str, k: int) -> str : Retrieve relevant chunks and generate a response.
"""

from typing import List, Optional
import numpy as np

from src.loaders.base_loader import BaseLoader, Document
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.base_embeddings import BaseEmbedder
from src.vectorstores.base_vectorstore import BaseVectorStore, PersistableStore
from src.rag.retriever import Retriever
from src.rag.reranker import Reranker
from src.llm.base import BaseLLM
from langsmith import traceable


class Pipeline:

    def __init__(self, loaders: List[BaseLoader], cleaner: TextCleaner, splitter: TextSplitter, embedder: BaseEmbedder, vectorstore: BaseVectorStore, retriever: Retriever, generator: BaseLLM, reranker: Optional[Reranker] = None, relevance_threshold: Optional[float] = None, storage_path: str = "backend/data/processed/faiss"):
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

        Args:
            query (str): User question to answer.
            k (int): Number of chunks to retrieve. Defaults to 5.

        Returns:
            str: Generated response from the LLM.
        """
        # Retrieve more candidates if reranking afterwards
        retrieve_k = k * 2 if self.reranker else k
        documents = self.retriever.retrieve(query, k=retrieve_k)
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