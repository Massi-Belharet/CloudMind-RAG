"""
One-time index build script for CloudMind RAG API (Sprint 5).

Loads all cloud documents (PDF, Markdown, CSV), embeds them with the production
embedding model (BAAI/bge-m3, per ADR 003) at the production chunk size, and
indexes them into the persistent Qdrant collection used by the API. Qdrant
persists across restarts via its Docker volume, so this script only needs to
run once — the API itself never re-indexes at startup.

Functions:
    run_build() -> None : Load, clean, split, embed and index the full corpus into Qdrant.
"""

from src.loaders.pdf_loader import PDFLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.csv_loader import CSVLoader
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.embedder import Embedder
from src.vectorstores.qdrant_store import QdrantStore
from src.utils.config import config

COLLECTION_NAME = config.api.collection_name


def run_build() -> None:
    """
    Load, clean, split, embed and index the full CloudMind corpus into the
    production Qdrant collection.
    """
    print("CloudMind — Production Index Build")
    print(f"Embedding model : {config.embedding.model}")
    print(f"Chunk size      : {config.rag.chunk_size}")
    print(f"Collection      : {COLLECTION_NAME}")

    print("\nLoading documents...")
    documents = []
    documents.extend(PDFLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(MarkdownLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(CSVLoader(config.benchmark.csv_path).load())

    documents = TextCleaner().clean(documents)
    chunks = TextSplitter(
        chunk_size=config.rag.chunk_size,
        chunk_overlap=config.rag.chunk_overlap
    ).split(documents)
    print(f"{len(chunks)} chunks ready")

    print("\nEmbedding chunks...")
    embedder = Embedder(model_name=config.embedding.model, use_fp16=True)
    vectors = embedder.embed(chunks)

    print("\nIndexing into Qdrant...")
    store = QdrantStore(collection_name=COLLECTION_NAME, embedding_dim=config.embedding.dim)
    store.add(chunks, vectors)

    print(f"\nProduction collection '{COLLECTION_NAME}' ready ({len(chunks)} chunks)")


if __name__ == "__main__":
    run_build()
