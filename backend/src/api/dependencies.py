"""
Dependency injection 

Builds the production Advanced RAG pipeline once and reuses the same instance
for every subsequent request, avoiding reloading models (bge-m3,
bge-reranker-v2-m3) or reconnecting to Qdrant on every call.

Functions:
    get_pipeline() -> Pipeline : Return the cached production RAG pipeline.
"""

from functools import lru_cache

import torch  

from langchain_ollama import ChatOllama

from src.loaders.pdf_loader import PDFLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.csv_loader import CSVLoader
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.embedder import Embedder
from src.vectorstores.qdrant_store import QdrantStore
from src.rag.retriever import Retriever
from src.rag.hybrid_retriever import HybridRetriever
from src.rag.multi_query_retriever import MultiQueryRetriever
from src.rag.reranker import Reranker
from src.rag.pipeline import Pipeline
from src.llm.generator import Generator
from src.utils.config import config
from src.utils.settings import settings


@lru_cache
def get_pipeline() -> Pipeline:
    """
    Build the production RAG pipeline once and cache it for reuse across requests.

    Loads and splits the corpus in memory for HybridRetriever's BM25 index.
    This does not re-embed or re-index anything — the vectors already live in
    Qdrant's production collection, populated ahead of time by build_index.py.

    Returns:
        Pipeline: The fully assembled production RAG pipeline.
    """
    documents = []
    documents.extend(PDFLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(MarkdownLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(CSVLoader(config.benchmark.csv_path).load())

    documents = TextCleaner().clean(documents)
    chunks = TextSplitter(
        chunk_size=config.rag.chunk_size,
        chunk_overlap=config.rag.chunk_overlap
    ).split(documents)

    embedder = Embedder(model_name=config.embedding.model, use_fp16=True)
    store = QdrantStore(collection_name=config.api.collection_name, embedding_dim=config.embedding.dim)
    retriever = Retriever(embedder=embedder, vectorstore=store)
    hybrid = HybridRetriever(retriever=retriever, documents=chunks)

    ollama_base_url = f"http://{settings.ollama_host}:{settings.ollama_port}"
    llm_multi_query = ChatOllama(model=config.llm.multi_query_model, base_url=ollama_base_url)
    multi_query = MultiQueryRetriever(llm=llm_multi_query, retriever=hybrid)

    reranker = Reranker()

    llm_generator = ChatOllama(model=config.llm.model, base_url=ollama_base_url, think=False)
    generator = Generator(llm=llm_generator)

    return Pipeline(
        loaders=[],
        cleaner=TextCleaner(),
        splitter=TextSplitter(chunk_size=config.rag.chunk_size, chunk_overlap=config.rag.chunk_overlap),
        embedder=embedder,
        vectorstore=store,
        retriever=multi_query,
        generator=generator,
        reranker=reranker,
        relevance_threshold=config.rag.relevance_threshold,
    )