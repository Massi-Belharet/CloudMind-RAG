"""
Embedding Models Benchmark script for CloudMind RAG pipeline.

Compares nomic-ai/nomic-embed-text-v1.5 and BAAI/bge-m3 on indexing speed,
search latency, P95 latency, throughput and similarity scores.
Results are saved to backend/results/benchmarks/embedding_benchmark_results.{json,csv}

Functions:
    load_queries() -> List[str] : Load benchmark queries from JSON file.
    benchmark_embedding_model(model_config, chunks, queries) -> dict : Benchmark a single embedding model.
    run_benchmark() -> None : Run the full benchmark across all configured embedding models.
"""

import time
import json
import csv
from pathlib import Path
from typing import List

import numpy as np
import torch

from src.loaders.pdf_loader import PDFLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.csv_loader import CSVLoader
from src.preprocessing.cleaners import TextCleaner
from src.preprocessing.text_splitter import TextSplitter
from src.embeddings.embedder import Embedder
from src.vectorstores.qdrant_store import QdrantStore
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


def benchmark_embedding_model(model_config, chunks: List[Document], queries: List[str]) -> dict:
    """
    Benchmark a single embedding model on indexing speed, search latency and similarity.

    Args:
        model_config: EmbeddingModelConfig with name and dim.
        chunks (List[Document]): Pre-loaded document chunks to index.
        queries (List[str]): List of query strings to search.

    Returns:
        dict: Benchmark results for this embedding model.
    """
    print(f"\n{'='*55}")
    print(f"Benchmarking : {model_config.name}")
    print(f"Dimension    : {model_config.dim}")
    print(f"{'='*55}")

    embedder = Embedder(model_name=model_config.name, use_fp16=model_config.use_fp16)

    collection_name = f"benchmark_emb_{model_config.name.split('/')[-1].replace('-', '_').replace('.', '_')}"

    # 1. Indexing
    print("Embedding chunks...")
    embed_start = time.perf_counter()
    texts = [model_config.document_prefix + doc.content for doc in chunks]
    vectors = embedder.model.encode(texts, show_progress_bar=True, batch_size=model_config.batch_size).astype(np.float32)
    embedding_time = round(time.perf_counter() - embed_start, 4)
    print(f"✅ Embedding time  : {embedding_time}s")

    store = QdrantStore(collection_name=collection_name, embedding_dim=model_config.dim)

    index_start = time.perf_counter()
    store.add(chunks, vectors)
    indexing_time = round(time.perf_counter() - index_start, 4)
    print(f"✅ Indexing time   : {indexing_time}s")

    # 2. Search speed + scores
    individual_times = []
    all_scores = []

    for _ in range(config.benchmark.n_runs):
        for query in queries:
            query_vector = embedder.model.encode([model_config.query_prefix + query])[0]
            t0 = time.perf_counter()
            results = store.search(query_vector, k=config.benchmark.top_k)
            individual_times.append(time.perf_counter() - t0)
            all_scores.extend([r.metadata.get("similarity_score", 0) for r in results])

    avg_search_time = round(float(np.mean(individual_times)), 4)
    p95_latency = round(float(np.percentile(individual_times, 95)), 4)
    throughput = round(1.0 / float(np.mean(individual_times)), 2)
    avg_score = round(float(np.mean(all_scores)) if all_scores else 0, 4)

    print(f"✅ Avg search time : {avg_search_time}s")
    print(f"✅ P95 latency     : {p95_latency}s")
    print(f"✅ Throughput      : {throughput} QPS")
    print(f"✅ Avg similarity  : {avg_score}")

    # 3. Cleanup
    store.client.delete_collection(collection_name)
    del embedder
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return {
        "model": model_config.name,
        "dim": model_config.dim,
        "n_documents": len(chunks),
        "n_queries": len(queries),
        "embedding_time_s": embedding_time,
        "indexing_time_s": indexing_time,
        "avg_search_time_s": avg_search_time,
        "p95_latency_s": p95_latency,
        "throughput_qps": throughput,
        "avg_similarity_score": avg_score
    }


def run_benchmark() -> None:
    """
    Run the embedding models benchmark across all models defined in config.
    Loads all Cloud documents, runs each model and saves results.
    Results are saved to backend/results/benchmarks/.
    """
    print("🚀 CloudMind — Embedding Models Benchmark")
    print(f"Models  : {[m.name for m in config.benchmark.embedding_models]}")
    print(f"N runs  : {config.benchmark.n_runs}")

    # Load + preprocess documents
    print("\n📥 Loading documents...")
    documents = []
    documents.extend(PDFLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(MarkdownLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(CSVLoader(config.benchmark.csv_path).load())

    documents = TextCleaner().clean(documents)
    chunks = TextSplitter(
        chunk_size=config.benchmark.chunk_size,
        chunk_overlap=config.rag.chunk_overlap
    ).split(documents)
    print(f"✅ {len(chunks)} chunks ready")

    # Load queries
    queries = load_queries()
    print(f"✅ {len(queries)} queries loaded")

    # Run benchmark for each model
    results = []
    for model_config in config.benchmark.embedding_models:
        result = benchmark_embedding_model(model_config, chunks, queries)
        results.append(result)

    # Save results
    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    with open(results_path / "embedding_benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    with open(results_path / "embedding_benchmark_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Results saved to {results_path}")

    # Print summary
    print("\n📊 EMBEDDING BENCHMARK SUMMARY")
    print(f"{'Model':<35} {'Embed(s)':<12} {'Index(s)':<12} {'Search(s)':<12} {'P95(s)':<10} {'QPS':<10} {'Similarity':<10}")
    print("-" * 101)
    for r in results:
        model_short = r['model'].split('/')[-1]
        print(f"{model_short:<35} {r['embedding_time_s']:<12} {r['indexing_time_s']:<12} {r['avg_search_time_s']:<12} {r['p95_latency_s']:<10} {r['throughput_qps']:<10} {r['avg_similarity_score']:<10}")


if __name__ == "__main__":
    run_benchmark()