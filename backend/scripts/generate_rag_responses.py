"""
RAG Response Generation script for CloudMind pipeline (Sprint 4 — Part C, step 1).

Runs the production Advanced RAG stack (bge-m3 embeddings, Hybrid Search,
Multi-Query RAG-Fusion, Cross-Encoder Reranker, qwen3.5:9b generation) against
the manually annotated ground truth queries and saves each query's generated
response together with its retrieved contexts. Pipeline.ask() only returns the
final response string, so the components are assembled manually here to expose
the intermediate contexts required by ragas_evaluation.py (Part C, step 2).

Functions:
    load_ground_truth() -> List[dict] : Load annotated queries and reference answers.
    build_rag_stack(chunks: List[Document]) -> tuple : Assemble the retrieval and generation components.
    generate_responses(ground_truth, multi_query, reranker, generator) -> List[dict] : Run the RAG stack on each query.
    run_generation() -> None : Load data, build the RAG stack and generate all responses.
"""

import json
from pathlib import Path
from typing import List, Tuple

import torch  

from langchain_ollama import ChatOllama
from qdrant_client import QdrantClient

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
from src.llm.generator import Generator
from src.loaders.base_loader import Document
from src.utils.config import config
from src.utils.settings import settings


COLLECTION_NAME = "ragas_eval_bge_m3"


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


def build_rag_stack(chunks: List[Document]) -> Tuple[MultiQueryRetriever, Reranker, Generator]:
    """
    Assemble the production Advanced RAG stack using the current default embedding model.

    Args:
        chunks (List[Document]): Pre-loaded document chunks to index.

    Returns:
        Tuple[MultiQueryRetriever, Reranker, Generator]: The retrieval and generation components.
    """
    embedder = Embedder(model_name=config.embedding.model, use_fp16=True)
    vectors = embedder.embed(chunks)

    store = QdrantStore(collection_name=COLLECTION_NAME, embedding_dim=config.embedding.dim)
    store.add(chunks, vectors)

    retriever = Retriever(embedder=embedder, vectorstore=store)
    hybrid = HybridRetriever(retriever=retriever, documents=chunks)

    ollama_base_url = f"http://{settings.ollama_host}:{settings.ollama_port}"
    llm_multi_query = ChatOllama(model=config.llm.multi_query_model, base_url=ollama_base_url)
    multi_query = MultiQueryRetriever(llm=llm_multi_query, retriever=hybrid)

    reranker = Reranker()

    llm_generator = ChatOllama(
        model=config.llm.model,
        base_url=ollama_base_url,
        think=False,
        num_predict=2048,  # qwen3.5:9b spends tokens on internal reasoning; 2048 leaves room for the answer (1024 left some responses empty/truncated)
    )
    generator = Generator(llm=llm_generator)

    return multi_query, reranker, generator


def generate_responses(
    ground_truth: List[dict],
    multi_query: MultiQueryRetriever,
    reranker: Reranker,
    generator: Generator
) -> List[dict]:
    """
    Run the RAG stack on each ground truth query and collect responses with their contexts.

    Mirrors Pipeline.ask()'s retrieve-then-rerank logic (retrieve 2*top_k candidates
    before reranking down to top_k) so results reflect real production behavior.

    Args:
        ground_truth (List[dict]): Annotated queries with reference answers.
        multi_query (MultiQueryRetriever): Retriever combining RAG-Fusion and hybrid search.
        reranker (Reranker): Cross-encoder reranker.
        generator (Generator): LLM response generator.

    Returns:
        List[dict]: Entries with 'query', 'response', 'contexts' and 'reference_answer'.
    """
    results = []
    top_k = config.rag.top_k

    for i, entry in enumerate(ground_truth, start=1):
        query = entry["query"]
        print(f"\n[{i}/{len(ground_truth)}] {query}")

        candidates = multi_query.retrieve(query, k=top_k * 2)
        reranked = reranker.rerank(query, candidates, top_k=top_k)
        response = generator.generate(query, reranked)

        print(f"Response generated ({len(reranked)} contexts)")

        results.append({
            "query": query,
            "response": response,
            "contexts": [doc.content for doc in reranked],
            "reference_answer": entry["reference_answer"],
        })

    return results


def run_generation() -> None:
    """
    Load documents and ground truth, build the production RAG stack and generate
    responses for every annotated query. Results are saved to
    backend/results/benchmarks/rag_generation_output.json.
    """
    print("CloudMind — RAG Response Generation (Part C, step 1)")
    print(f"Embedding model : {config.embedding.model}")
    print(f"Generator model : {config.llm.model}")
    print(f"Multi-query LLM : {config.llm.multi_query_model}")

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

    ground_truth = load_ground_truth()
    print(f"{len(ground_truth)} annotated queries loaded")

    print("\nBuilding RAG stack...")
    multi_query, reranker, generator = build_rag_stack(chunks)

    print("\nGenerating responses...")
    results = generate_responses(ground_truth, multi_query, reranker, generator)

    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    output_path = results_path / "rag_generation_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_path}")

    # Cleanup
    client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted")


if __name__ == "__main__":
    run_generation()