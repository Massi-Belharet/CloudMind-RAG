# CloudMind RAG

> Prescriptive RAG system for FinOps optimization in Multi-cloud architectures.

## Overview

CloudMind is an Advanced RAG pipeline that helps teams make informed decisions
about their cloud infrastructure by querying official documentation, best practices,
and FinOps data from AWS, Azure, GCP and compliance sources.

## Sprint 1 — Naive RAG 

### What's implemented

- PDF, Markdown and CSV document loaders
- Text cleaning and chunking (recursive + markdown structure-aware)
- Embeddings (nomic-embed-text-v1.5)
- FAISS vector store with HNSW index and cosine similarity
- End-to-end RAG pipeline (load → clean → split → embed → index → retrieve → generate)
- Local LLM via Ollama (qwen3.5:9b)
- Full unit test coverage

### Stack

| Component | Technology |
|---|---|
| Language | Python 3.11+ |
| PDF Loader | PyMuPDF |
| Text Splitting | LangChain Text Splitters |
| Embeddings | nomic-embed-text-v1.5 |
| Vector Store | FAISS (IndexHNSWFlat) |
| LLM | qwen3.5:9b via Ollama |
| Testing | pytest |

## Project Structure

\```
backend/
├── src/
│   ├── loaders/         # PDF, Markdown, CSV loaders
│   ├── preprocessing/   # Text cleaner + splitter
│   ├── embeddings/      # Embedder
│   ├── vectorstores/    # FAISS vector store
│   ├── rag/             # Retriever + Pipeline
│   └── llm/             # Generator + Prompts
├── data/raw/
│   ├── cloud_docs/aws/
│   ├── cloud_docs/azure/
│   ├── cloud_docs/gcp/
│   └── cloud_docs/compliance/
├── tests/unit/
└── notebooks/
\```

## Installation

\```bash
git clone https://github.com/Massi-Belharet/CloudMind-RAG.git
cd CloudMind-RAG
uv sync
\```