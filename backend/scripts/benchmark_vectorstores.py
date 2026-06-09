"""
Vector Stores Benchmark 

Measures and compares indexing speed, search speed, P95 latency, throughput
and similarity scores across FAISS, Qdrant, and Pgvector.
Results are saved to backend/results/benchmarks/

Functions:
    load_queries() -> List[str] : Load benchmark queries from JSON file.
    benchmark_store(store_name, store, vectors, documents, query_vectors) -> dict : Benchmark a single vector store.
    run_benchmark() -> None : Run the full benchmark across all three stores.
"""

import time
import json
import csv
from pathlib import Path
from typing import List

import numpy as np

from src.loaders.pdf_loader import PDFLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.csv_loader import CSVLoader
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.embedder import Embedder
from src.vectorstores.faiss_store import FAISSStore
from src.vectorstores.qdrant_store import QdrantStore
from src.vectorstores.pgvector_store import PgvectorStore
from src.loaders.base_loader import Document
from src.utils.config import config


def load_queries() -> List[str]:
    """
    Load benchmark queries from the queries JSON file.

    Returns:
        List[str]: List of query strings.

    Raises:
        FileNotFoundError: If the queries file does not exist.
    """
    path = Path(config.benchmark.queries_path)
    if not path.exists():
        raise FileNotFoundError(f"Queries file not found: {path}")

    with open(path, "r") as f:
        data = json.load(f)

    return data["vector_stores_benchmark"]


def benchmark_store(
    store_name: str,
    store,
    vectors: np.ndarray,
    documents: List[Document],
    query_vectors: np.ndarray
) -> dict:
    """
    Benchmark a single vector store for indexing speed, search speed,
    P95 latency, throughput and similarity.

    Args:
        store_name (str): Name of the vector store (faiss, qdrant, pgvector).
        store: Vector store instance.
        vectors (np.ndarray): Embedding matrix to index.
        documents (List[Document]): Documents to index.
        query_vectors (np.ndarray): Query vectors to search.

    Returns:
        dict: Benchmark results with indexing time, search time, P95, QPS and similarity scores.
    """
    print(f"\n{'='*50}")
    print(f"Benchmarking {store_name.upper()}")
    print(f"{'='*50}")

    # 1. Indexing speed
    start = time.perf_counter()
    store.add(documents, vectors)
    indexing_time = round(time.perf_counter() - start, 4)
    print(f"Indexing time  : {indexing_time}s")

    # 2. Search speed + scores
    search_times = []
    all_scores = []
    individual_times = []

    for _ in range(config.benchmark.n_runs):
        start = time.perf_counter()
        for query_vec in query_vectors:
            t0 = time.perf_counter()
            results = store.search(query_vec, k=config.benchmark.top_k)
            individual_times.append(time.perf_counter() - t0)
            all_scores.extend([
                r.metadata.get("similarity_score", 0) for r in results
            ])
        search_times.append(time.perf_counter() - start)

    avg_search_time = round(float(np.mean(search_times)), 4)
    p95_latency = round(float(np.percentile(individual_times, 95)), 4)
    throughput = round(len(query_vectors) / float(np.mean(search_times)), 2)
    avg_score = round(float(np.mean(all_scores)) if all_scores else 0, 4)

    print(f"Avg search time: {avg_search_time}s ({config.benchmark.n_runs} runs)")
    print(f"P95 latency    : {p95_latency}s")
    print(f"Throughput     : {throughput} QPS")
    print(f"Avg similarity : {avg_score}")

    return {
        "store": store_name,
        "n_documents": len(documents),
        "n_queries": len(query_vectors),
        "indexing_time_s": indexing_time,
        "avg_search_time_s": avg_search_time,
        "p95_latency_s": p95_latency,
        "throughput_qps": throughput,
        "avg_similarity_score": avg_score
    }


def run_benchmark() -> None:
    """
    Run the full benchmark across FAISS, Qdrant and Pgvector.
    Loads all Cloud documents (PDF, Markdown, CSV), embeds them and measures performance.
    Results are saved to backend/results/benchmarks/.
    """
    print("CloudMind — Vector Stores Benchmark")
    print(f"Embedding model : {config.embedding.model}")
    print(f"N runs          : {config.benchmark.n_runs}")

    # Load + preprocess
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

    # Embed
    print("\nEmbedding chunks...")
    embedder = Embedder(model_name=config.embedding.model)
    vectors = embedder.embed(chunks)
    print(f"Vectors shape: {vectors.shape}")

    # Embed queries
    queries = load_queries()
    query_vectors = np.array([embedder.embed_query(q) for q in queries])

    # Run benchmarks
    results = []

    results.append(benchmark_store(
        "faiss",
        FAISSStore(collection_name="benchmark_faiss", embedding_dim=config.embedding.dim),
        vectors, chunks, query_vectors
    ))

    qdrant_store = QdrantStore(
        collection_name="benchmark_qdrant",
        embedding_dim=config.embedding.dim
    )
    results.append(benchmark_store("qdrant", qdrant_store, vectors, chunks, query_vectors))

    results.append(benchmark_store(
        "pgvector",
        PgvectorStore(collection_name="benchmark_pgvector", embedding_dim=config.embedding.dim),
        vectors, chunks, query_vectors
    ))

    # Cleanup Qdrant
    qdrant_store.client.delete_collection("benchmark_qdrant")

    # Save results
    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    with open(results_path / "benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    with open(results_path / "benchmark_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {results_path}")

    # Print summary
    print("\nBENCHMARK SUMMARY")
    print(f"{'Store':<12} {'Indexing(s)':<14} {'Search(s)':<12} {'P95(s)':<10} {'QPS':<10} {'Similarity':<10}")
    print("-" * 68)
    for r in results:
        print(f"{r['store']:<12} {r['indexing_time_s']:<14} {r['avg_search_time_s']:<12} {r['p95_latency_s']:<10} {r['throughput_qps']:<10} {r['avg_similarity_score']:<10}")


if __name__ == "__main__":
    run_benchmark()