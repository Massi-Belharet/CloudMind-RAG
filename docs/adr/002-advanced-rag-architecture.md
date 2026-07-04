# ADR 002 — Advanced RAG Architecture for CloudMind

## Status
Accepted

## Date
2026-06-17

## Context

Following Sprint 2 (vector store selection — ADR 001), Sprint 3 introduces Advanced RAG
techniques to improve retrieval quality and generation accuracy in the CloudMind FinOps pipeline.

The naive RAG pipeline (Sprint 1) retrieved chunks by dense similarity only, which missed
exact keyword matches for technical FinOps terms (EC2 instance types, pricing regions, etc.)
and had no mechanism to detect irrelevant or out-of-scope queries.

## Decisions

### 1. Hybrid Search — BM25 + Dense + RRF

**Decision** : Combine BM25 lexical search with dense semantic search using Reciprocal Rank Fusion.

**Rationale** :
- Dense search alone misses exact technical terms ("EC2 t3.medium", "us-east-1", "RGPD article 28")
- BM25 alone misses semantic meaning ("reduce spending" ≠ "cost optimization")
- RRF fusion captures both signals without requiring score normalization
- Implementation uses `rank_bm25` (BM25Okapi) + QdrantStore + shared `rrf_fusion()` module

### 2. Cross-Encoder Reranker — BAAI/bge-reranker-v2-m3

**Decision** : Re-score retrieved chunks using a cross-encoder before generation.

**Rationale** :
- Embedding similarity compares vectors independently — less precise than joint evaluation
- Cross-encoder evaluates (query, document) pairs jointly → more accurate relevance scores
- `BAAI/bge-reranker-v2-m3` selected for multilingual support (FR/EN) and strong performance
- Integrated as optional component in Pipeline — activated via `reranker` parameter

### 3. Multi-Query RAG-Fusion — llama3.2:1b

**Decision** : Generate multiple semantically distinct query reformulations and fuse results with RRF.

**Rationale** :
- Single query retrieval misses relevant chunks framed differently in documentation
- RAG-Fusion (Multi-Query + RRF) captures more signal than simple deduplication
- `llama3.2:1b` selected for reformulation — no thinking mode, ultra lightweight (~600MB VRAM)
- `qwen3.5:2b` rejected — inconsistent output with thinking mode (103s, empty responses)
- `qwen3.5:9b` retained for final response generation (quality over speed)
- RRF extracted into shared `fusion.py` module — reused by HybridRetriever and MultiQueryRetriever

### 4. Semantic Router — Embedding-based with Threshold

**Decision** : Route queries to the relevant cloud provider namespace using cosine similarity.

**Rationale** :
- LLM-based routing rejected — adds 1-2s latency per request with a 3rd LLM call
- Embedding-based routing reuses the existing embedder (~50ms overhead)
- Threshold of 0.6 with `nomic-embed-text-v1.5` correctly routes AWS, Azure, GCP, compliance queries
- Returns `None` for general queries → no filter applied → searches all providers

**Update (Sprint 5)** : The router was built and tested in Sprint 3 but never wired into
`dependencies.py` — it existed in the codebase without being called in production. This
allowed cross-provider contamination in retrieval (e.g. GCP-sourced chunks appearing in
an AWS-specific answer). It is now wired end-to-end: `Pipeline.ask()`/`ask_stream()` call
`router.route(query)` once on the original query (not on Multi-Query reformulations), and
the resulting provider (or `None`) is threaded through `Retriever` → `HybridRetriever` →
`QdrantStore.search(filter_provider=...)`. BM25 results are filtered post-hoc by metadata
since the BM25 index isn't partitioned by provider. See ADR 003's Consequences section
for the threshold recalibration this required after the switch to bge-m3.

### 5. CRAG — Corrective RAG

**Decision** : Evaluate retrieval relevance before generation using reranker scores.

**Rationale** :
- Naive RAG generates responses even for out-of-scope queries → hallucinations
- CRAG uses existing CrossEncoder scores (avg rerank score vs threshold)
- Below threshold → fallback message without LLM call (~0.36s vs ~60s)
- Integrated directly in `Pipeline.ask()` via `relevance_threshold` parameter

### 6. Observability — LangSmith

**Decision** : Enable LangSmith tracing via environment variables + `@traceable` on `Pipeline.ask()`.

**Rationale** :
- LangChain auto-traces ChatOllama calls via `LANGSMITH_TRACING=true`
- `@traceable` adds Pipeline.ask() as parent span for full pipeline visibility
- No code instrumentation needed for LLM calls — zero overhead approach

## Consequences

- All Advanced RAG components are optional and injectable → Pipeline stays flexible
- Sprint 4 will benchmark embedding models (nomic-v1.5 vs bge-m3) using this fixed pipeline
- RAGAS evaluation (Recall@K, Faithfulness, Answer Relevancy) deferred to Sprint 4 completed, see ADR 003 Part B and Part C
- LangSmith traces available at https://smith.langchain.com → project CloudMind-RAG

## Observed Latency (Integration Tests)

| Component | Latency |
|---|---|
| SemanticRouter | ~50ms |
| MultiQuery (llama3.2:1b) | 1-8s |
| Reranker (bge-reranker-v2-m3) | ~2-5s |
| Generator (qwen3.5:9b) | ~60-70s |
| CRAG fallback (no LLM) | ~0.36s |

## Future Evaluation

Sprint 4 will evaluate the complete Advanced RAG pipeline using RAGAS :

- **Recall@K** — percentage of relevant chunks retrieved
- **NDCG@K** — ranking quality of retrieved results
- **Context Precision** — relevance of retrieved chunks
- **Context Recall** — coverage of relevant information
- **Faithfulness** — answer grounded in context
- **Answer Relevancy** — answer addresses the question
- **Correctness** — factual accuracy vs ground truth

These metrics will be computed on a ground truth dataset generated by RAGAS TestsetGenerator,
comparing Naive RAG (Sprint 1) vs Advanced RAG (Sprint 3) on the fixed Qdrant vector store.