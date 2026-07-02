# ADR 003 — Embedding Model Choice for CloudMind

## Status
Accepted

## Date
2026-06-28

## Context

Following ADR 001 (Qdrant as vector store) and ADR 002 (Advanced RAG architecture),
Sprint 4 evaluates which embedding model should power CloudMind in production.

Three candidates were evaluated: **nomic-embed-text-v1.5** (baseline used since Sprint 1),
**BAAI/bge-m3** (originally intended production model), and **Qwen3-Embedding-0.6B**
(lightweight modern challenger).

The evaluation was split into two independent parts to avoid a known pitfall — raw
cosine similarity scores are measured within each model's own embedding space and
are not directly comparable across models.

## Evaluation Methodology

### Part A — Infrastructure Benchmark
Same fixed pipeline as Sprint 2 (Qdrant, 7,219 chunks from cloud_docs PDF/Markdown/CSV,
10 queries). Metrics: embedding time, indexing time, average search time, P95 latency,
throughput (QPS), average similarity score.

### Part B — Retrieval Quality (Ground Truth Based)
10 manually annotated queries (`backend/data/benchmark/ground_truth.json`), each with
a known relevant source document and a reference answer. A retrieved chunk counts as
relevant if its `file_name` matches the annotated document (document-level matching).
Metrics computed manually — Recall@5 (Hit@5), MRR, NDCG@5. RAGAS `TestsetGenerator`
was not used to build this ground truth, as it is known to hang with local Ollama models.

## Results

### Part A — Infrastructure

| Model | Embed Time | Index Time | Avg Search | P95 | QPS | Similarity |
|---|---|---|---|---|---|---|
| nomic-embed-text-v1.5 | 219.41s | 8.75s | 0.0161s | 0.0299s | 62.17 | 0.7509 |
| BAAI/bge-m3 | 110.24s | 7.94s | 0.0211s | 0.0311s | 47.34 | 0.6590 |
| Qwen3-Embedding-0.6B | 357.24s | 8.93s | 0.0151s | 0.0262s | 66.08 | 0.6888 |

### Part B — Retrieval Quality (n=10 queries)

| Model | Recall@5 | MRR | NDCG@5 |
|---|---|---|---|
| nomic-embed-text-v1.5 | 0.70 | 0.4233 | 0.4905 |
| **BAAI/bge-m3** | **0.70** | **0.5500** | **0.5893** |
| Qwen3-Embedding-0.6B | 0.50 | 0.3533 | 0.3887 |

## Decision

**BAAI/bge-m3** is selected as the production embedding model for CloudMind.

## Rationale

**Why not rely on avg_similarity_score alone (Part A)?**
Part A suggested nomic-embed-text-v1.5 was best (0.7509 vs 0.6590 for bge-m3). This is
misleading — cosine similarity is not comparable across models with different training
objectives and embedding spaces. This is precisely why Part B was necessary before
making a production decision.

**Why not nomic-embed-text-v1.5?**
Despite tying on Recall@5 (0.70), it has a meaningfully lower MRR (0.4233 vs 0.5500)
and NDCG@5 (0.4905 vs 0.5893) — the relevant document is retrieved less consistently
at the top of the ranking. It is also nearly 2x slower to embed the full corpus.

**Why not Qwen3-Embedding-0.6B?**
Despite being lightweight and multilingual, it underperformed on every retrieval
quality metric and was the slowest to embed (357s) due to its instruction-based query
prefix. Not retained.

**Why BAAI/bge-m3?**
- Best MRR (0.55) and NDCG@5 (0.5893) — relevant documents rank higher, more consistently
- Ties for the best Recall@5 (0.70) — no retrieval coverage sacrificed
- Fastest embedding time (110s) — 2x faster than nomic-v1.5, relevant for `build()` indexing
- Natively multilingual — matches CloudMind's FR/EN usage
- Was the intended production candidate since Sprint 2 planning

## Consequences

- `config.yaml` `embedding.model` must be updated to `BAAI/bge-m3` (dim=1024) for production
- Qdrant collections must be rebuilt with 1024-dim vectors instead of 768-dim
- `use_fp16` must stay enabled for bge-m3 on 8GB VRAM (RTX 4060) to avoid CUDA OOM,
  as established during Part A/B debugging
- SemanticRouter's threshold (currently 0.6, tuned against nomic-v1.5's similarity
  distribution) will need re-validation against bge-m3's distribution before Sprint 5
- All Advanced RAG components (HybridRetriever, MultiQueryRetriever, Reranker) remain
  embedding-model agnostic by design (ADR 002) — no code changes required beyond config

## Future Evaluation

Sprint 4 Part C will evaluate the complete RAG pipeline using BAAI/bge-m3 with
`ragas.evaluate()` (not `TestsetGenerator`) :

- **Faithfulness** — is the generated answer grounded in retrieved context?
- **Answer Relevancy** — does the answer address the question?
- **Context Precision** — are retrieved chunks relevant to the query?
- **Context Recall** — is the reference answer's information covered by retrieved context?

These metrics will use the `reference_answer` field already present in
`ground_truth.json`, with `qwen3.5:9b` as the LLM judge (temperature=0 for reproducibility).