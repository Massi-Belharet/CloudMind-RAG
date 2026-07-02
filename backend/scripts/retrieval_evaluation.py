"""
Retrieval Quality Evaluation script for CloudMind RAG pipeline (Sprint 4 — Part B).

Evaluates retrieval quality of each embedding model using classic IR metrics
computed against a manually annotated ground truth (document-level relevance).
No ragas here — pure IR metrics. Ragas-based generation evaluation lives in
ragas_evaluation.py (Part C).

Metrics (single relevant document per query, binary relevance):
    Recall@K (Hit@K) : 1 if the relevant document appears in the top-K, else 0.
    MRR              : 1 / rank of the first relevant chunk (0 if absent).
    NDCG@K           : 1 / log2(rank + 1) if found (IDCG = 1), else 0.

Ranks are 1-indexed. Results are saved to
backend/results/benchmarks/retrieval_evaluation_results.{json,csv}

Functions:
    load_ground_truth() -> List[dict] : Load annotated queries and relevant docs.
    compute_metrics(retrieved_docs, relevant_doc, k) -> dict : IR metrics for one query.
    evaluate_embedding_model(model_config, chunks, ground_truth) -> dict : Evaluate one model.
    run_evaluation() -> None : Run evaluation across all configured embedding models.
"""

import json
import csv
import math
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


def load_ground_truth() -> List[dict]:
    """
    Load the manually annotated ground truth file.

    Returns:
        List[dict]: List of entries with 'query', 'relevant_doc' and 'reference_answer'.

    Raises:
        FileNotFoundError: If the ground truth file does not exist.
    """
    path = Path(config.benchmark.ground_truth_path)
    if not path.exists():
        raise FileNotFoundError(f"Ground truth file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_metrics(retrieved_docs: List[Document], relevant_doc: str, k: int) -> dict:
    """
    Compute Recall@K (Hit@K), MRR and NDCG@K for a single query.

    A retrieved chunk is relevant if its file_name matches relevant_doc.
    Since there is exactly one relevant document with binary relevance,
    IDCG = 1 and NDCG collapses to 1 / log2(rank + 1).

    Args:
        retrieved_docs (List[Document]): Top-K documents returned by the retriever, ordered.
        relevant_doc (str): File name of the ground-truth relevant document.
        k (int): Cut-off rank.

    Returns:
        dict: {'recall_at_k', 'mrr', 'ndcg_at_k'} for this query.
    """
    rank = None
    for i, doc in enumerate(retrieved_docs[:k]):
        if doc.metadata.get("file_name") == relevant_doc:
            rank = i + 1  # 1-indexed
            break

    if rank is None:
        return {"recall_at_k": 0.0, "mrr": 0.0, "ndcg_at_k": 0.0}

    return {
        "recall_at_k": 1.0,
        "mrr": 1.0 / rank,
        "ndcg_at_k": 1.0 / math.log2(rank + 1),
    }


def evaluate_embedding_model(model_config, chunks: List[Document], ground_truth: List[dict]) -> dict:
    """
    Evaluate a single embedding model's retrieval quality against the ground truth.

    Args:
        model_config: EmbeddingModelConfig with name, dim, prefixes, batch_size, use_fp16.
        chunks (List[Document]): Pre-loaded document chunks to index.
        ground_truth (List[dict]): Annotated queries with relevant documents.

    Returns:
        dict: Averaged retrieval metrics for this embedding model.
    """
    print(f"\n{'='*55}")
    print(f"Evaluating : {model_config.name}")
    print(f"Dimension  : {model_config.dim}")
    print(f"{'='*55}")

    embedder = Embedder(model_name=model_config.name, use_fp16=model_config.use_fp16)

    collection_name = f"eval_retrieval_{model_config.name.split('/')[-1].replace('-', '_').replace('.', '_')}"

    # Index chunks
    print("Embedding chunks...")
    texts = [model_config.document_prefix + doc.content for doc in chunks]
    vectors = embedder.model.encode(
        texts, show_progress_bar=True, batch_size=model_config.batch_size
    ).astype(np.float32)

    store = QdrantStore(collection_name=collection_name, embedding_dim=model_config.dim)
    store.add(chunks, vectors)

    # Evaluate each query
    k = config.benchmark.top_k
    recalls, mrrs, ndcgs = [], [], []

    for entry in ground_truth:
        query_vector = embedder.model.encode([model_config.query_prefix + entry["query"]])[0]
        retrieved = store.search(query_vector, k=k)
        metrics = compute_metrics(retrieved, entry["relevant_doc"], k)
        recalls.append(metrics["recall_at_k"])
        mrrs.append(metrics["mrr"])
        ndcgs.append(metrics["ndcg_at_k"])

    avg_recall = round(float(np.mean(recalls)), 4)
    avg_mrr = round(float(np.mean(mrrs)), 4)
    avg_ndcg = round(float(np.mean(ndcgs)), 4)

    print(f"Recall@{k} : {avg_recall}")
    print(f"MRR       : {avg_mrr}")
    print(f"NDCG@{k}  : {avg_ndcg}")

    # Cleanup
    store.client.delete_collection(collection_name)
    del embedder
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return {
        "model": model_config.name,
        "dim": model_config.dim,
        "n_queries": len(ground_truth),
        "top_k": k,
        f"recall_at_{k}": avg_recall,
        "mrr": avg_mrr,
        f"ndcg_at_{k}": avg_ndcg,
    }


def run_evaluation() -> None:
    """
    Run the retrieval quality evaluation across all embedding models in config.
    Loads all Cloud documents, evaluates each model against the ground truth and saves results.
    Results are saved to backend/results/benchmarks/.
    """
    print("CloudMind — Retrieval Quality Evaluation (Part B)")
    print(f"Models  : {[m.name for m in config.benchmark.embedding_models]}")
    print(f"Top-K   : {config.benchmark.top_k}")

    # Load + preprocess documents (same pipeline as the embedding benchmark)
    print("\nLoading documents...")
    documents = []
    documents.extend(PDFLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(MarkdownLoader(config.benchmark.cloud_docs_path).load())
    documents.extend(CSVLoader(config.benchmark.csv_path).load())

    documents = TextCleaner().clean(documents)
    chunks = TextSplitter(
        chunk_size=config.benchmark.chunk_size,
        chunk_overlap=config.rag.chunk_overlap
    ).split(documents)
    print(f"{len(chunks)} chunks ready")

    # Load ground truth
    ground_truth = load_ground_truth()
    print(f"{len(ground_truth)} annotated queries loaded")

    # Evaluate each model
    results = []
    for model_config in config.benchmark.embedding_models:
        results.append(evaluate_embedding_model(model_config, chunks, ground_truth))

    # Save results
    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    with open(results_path / "retrieval_evaluation_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open(results_path / "retrieval_evaluation_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {results_path}")

    # Print summary
    k = config.benchmark.top_k
    print("\nRETRIEVAL EVALUATION SUMMARY")
    print(f"{'Model':<35} {'Recall@'+str(k):<12} {'MRR':<10} {'NDCG@'+str(k):<10}")
    print("-" * 67)
    for r in results:
        model_short = r["model"].split("/")[-1]
        print(f"{model_short:<35} {r[f'recall_at_{k}']:<12} {r['mrr']:<10} {r[f'ndcg_at_{k}']:<10}")


if __name__ == "__main__":
    run_evaluation()
