# ADR 001 — Vector Store Choice for CloudMind

## Status
Accepted

## Date
2026-06-09

## Context

CloudMind is a prescriptive FinOps RAG system that indexes 10,438 chunks from AWS, Azure, GCP 
and compliance documentation. The system needs a vector store that supports:

- Semantic similarity search for RAG retrieval
- Metadata filtering by cloud provider (AWS, Azure, GCP)
- Automatic persistence across restarts
- Production-grade performance for a multi-user application

Three vector stores were benchmarked : FAISS, Qdrant and Pgvector.

## Benchmark Results

| Store | Indexing | Avg Search | P95 Latency | Throughput | Similarity |
|---|---|---|---|---|---|
| FAISS | 0.23s | 0.003s | 0.0003s | 3603 QPS | 0.755 |
| Qdrant | 11.18s | 0.182s | 0.033s | 54.9 QPS | 0.755 |
| Pgvector | 24.22s | 0.514s | 0.060s | 19.45 QPS | 0.755 |

**Dataset** : 10,438 chunks — Embedding model : nomic-ai/nomic-embed-text-v1.5 (768 dim)

## Decision

**Qdrant** is selected as the production vector store for CloudMind.

## Rationale

**Why not FAISS ?**
Despite its exceptional performance (3,603 QPS), FAISS is an in-memory index, data is lost 
on restart without manual save/load operations. It also lacks native metadata filtering, 
which is critical for CloudMind to filter chunks by cloud provider (AWS/Azure/GCP).

**Why not Pgvector ?**
Pgvector's average search time of 0.514s exceeds the 200ms production threshold. 
While its P95 latency is acceptable, the SQL overhead makes it unsuitable as a 
primary vector store for a dedicated RAG pipeline.

**Why Qdrant ?**
- Search performance within production standards (0.182s avg, 0.033s P95) 
- Automatic persistence — no manual save/load required 
- Native metadata filtering by provider, document type and cost data 
- 54.9 QPS — sufficient for CloudMind's expected workload 
- Built-in dashboard for collection monitoring 
- Designed for production RAG workloads 

## Consequences

- FAISS remains available for local development and testing
- Pgvector remains available for future SQL + vector hybrid queries if needed
- Sprint 3 Advanced RAG features (Hybrid Search, filtering) will leverage Qdrant's metadata capabilities
- Embedding model benchmark (Sprint 4) will use Qdrant as the fixed vector store

## Future Evaluation

The current benchmark measures infrastructure performance metrics (latency, throughput, indexing speed).
Retrieval quality metrics will be evaluated in Sprint 4 :

**Evaluation metrics (RAGAS) :**
- **Recall@K** — percentage of relevant chunks retrieved
- **NDCG@K** — ranking quality of retrieved results
- **Context Precision** — relevance of retrieved chunks
- **Context Recall** — coverage of relevant information
- **Faithfulness** — answer grounded in context
- **Answer Relevancy** — answer addresses the question
- **Correctness** — factual accuracy vs ground truth

These metrics require a ground truth dataset that will be generated using RAGAS TestsetGenerator with the fixed Qdrant vector store and different embedding models.