# ADR 003 — Embedding Model Choice for CloudMind

## Status
Accepted

## Date
2026-07-03

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
- SemanticRouter's threshold needed re-validation against bge-m3's similarity
  distribution before Sprint 5 — done, see "Sprint 5 — Router Recalibration and
  CRAG Threshold Calibration" below
- All Advanced RAG components (HybridRetriever, MultiQueryRetriever, Reranker) remain
  embedding-model agnostic by design (ADR 002) — no code changes required beyond config

## Part C — RAG Pipeline Evaluation

The complete Advanced RAG pipeline (BAAI/bge-m3 embeddings, Hybrid Search,
Multi-Query RAG-Fusion, Cross-Encoder Reranker, qwen3.5:9b generation) was
evaluated with RAGAS using the `reference_answer` field from `ground_truth.json`.

**Production generation model deviation from this evaluation** : the Part C results
below were measured with `qwen3.5:9b` as the generator, per the pipeline described
above. In production (Sprint 5), the generator was switched to `llama3.1:8b` for
latency reasons, `qwen3.5:9b` takes ~60-94s per response due to its always-on
thinking overhead (confirmed with `think=False` still yielding ~86s, see verification
below), against ~25s for `llama3.1:8b` on the same query, measured via LangSmith
traces. This is the same thinking-mode limitation already identified for the
Multi-Query and RAGAS-judge roles above, now confirmed on free-form generation too.
The Faithfulness/Answer Relevancy/Context Precision/Context Recall scores below
therefore describe the pipeline as evaluated with `qwen3.5:9b`, not the exact model
currently serving production traffic, re-running this evaluation with `llama3.1:8b`
was not done due to time constraints. This is a known, accepted gap between what was
measured and what is deployed.

**Judge model deviation from initial plan** : `qwen3.5:9b` was initially planned
as the LLM judge but could not be used, it burns unbounded hidden reasoning
tokens even with `think=False`, so its structured-output calls to RAGAS's
prompts return empty regardless of `max_tokens`. This mirrors the same
thinking-mode issue documented in ADR 002 for Multi-Query reformulation.
`llama3.1:8b` was used instead — no hidden thinking overhead, reliably follows
RAGAS's JSON-based prompts.

**Embeddings for AnswerRelevancy** : RAGAS's legacy `AnswerRelevancy` metric
requires a LangChain-compatible embeddings interface. Rather than introduce a
separate embedding model/dependency, CloudMind's own `Embedder` (bge-m3) was
wrapped via a small `Embeddings` adapter, keeping a single source of truth for
embeddings across the whole project.

**Scope limitation** : Due to time constraints, this evaluation was run on
**5 of the 10** manually annotated ground truth queries, not the full set.
Results should be read as an initial signal, not a statistically complete
evaluation of the RAG pipeline. Extending to all 10 queries is a candidate
for future work if time permits before the project deadline.

### Results (n=5)

| Metric | Score |
|---|---|
| Faithfulness | 0.7724 |
| Answer Relevancy | 0.6914 |
| Context Precision | 0.7858 |
| Context Recall | 0.9778 |

### Interpretation

- **Context Recall (0.98)** is excellent — retrieved contexts almost always
  cover the information needed to reconstruct the reference answer.
- **Faithfulness (0.77)** is solid — generated answers are largely grounded
  in retrieved context, with limited hallucination.
- **Context Precision (0.79)** and **Answer Relevancy (0.69)** show room for
  improvement. One query ("Azure reserved instances") scored notably low on
  Context Precision (0.25) — the pipeline failed to surface the relevant
  chunk from the annotated source document for that specific phrasing,
  and the LLM correctly declined to answer rather than hallucinate,
  which validates CRAG's fallback behavior (ADR 002) is working as intended
  even outside the explicit fallback threshold path.

## Sprint 5 — Router Recalibration and CRAG Threshold Calibration

Two components inherited stale, uncalibrated defaults from earlier sprints. Both were
fixed empirically rather than by adjusting a single failing example.

### SemanticRouter threshold

The 0.6 threshold (ADR 002) was tuned against `nomic-embed-text-v1.5`'s similarity
distribution. After switching to `bge-m3` (this ADR), the router was found to be
disconnected from production entirely (see ADR 002 §4 update) — and once wired in,
0.6 no longer separated mono-provider from multi-provider queries correctly under
`bge-m3` (a clear AWS-specific query scored 0.588, just under threshold).

Root cause was not the threshold alone: `ROUTE_DESCRIPTIONS` (keyword-style, e.g.
`"aws ec2 s3"`) embedded poorly under `bge-m3` compared to natural-language phrasing.
Fix: rewrote `ROUTE_DESCRIPTIONS` as natural-language sentences (no change to
`route()`/`_cosine_similarity()`), then recalibrated on 22 queries (16 mono-provider,
6 explicitly multi-provider) via `backend/scripts/calibrate_router_threshold.py`.
New threshold: **0.5987** — zero dangerous false positives (no multi-provider query
was ever incorrectly filtered) across the test set. Configured via
`config.router.threshold`.

### CRAG relevance_threshold

`config.rag.relevance_threshold` was `0.0` — an untuned placeholder from Sprint 3,
functionally permissive since `bge-reranker-v2-m3` produces unbounded logits, not
0-1 probabilities. This let off-topic queries with superficial lexical overlap slip
past CRAG (e.g. "What is Python?" was answered from the LLM's general knowledge
instead of triggering the fallback, because "Python" appears in AWS/GCP SDK
documentation despite the question being unrelated to cloud/FinOps).

Calibrated via `backend/scripts/calibrate_crag_threshold.py` on 10 positive examples
(the ground truth queries) vs 10 negative examples (clearly out-of-scope, including
the "What is Python?" trap case). Score distributions: positives `[0.0145, 0.9899]`,
negatives `[0.0000, 0.0113]` — a clean separation. New threshold: **0.0129**. Results
saved to `backend/results/benchmarks/crag_threshold_calibration.json`.

### Verification

Both fixes were validated end-to-end post-recalibration:
- `"What is Python?"` → CRAG fallback triggered correctly (previously answered from
  general knowledge)
- `"What are the AWS Well-Architected Framework cost optimization pillars?"` (k=10)
  → AWS-only sources, no GCP contamination (previously mixed providers)
- `"How to optimize Kubernetes workloads for cost efficiency in a multi-cloud setup?"`
  → still correctly retrieves AWS + Azure + GCP sources (provider filter does not
  fire on genuinely multi-provider queries)

Full unit test suite (184/184) passes after both changes, including updated coverage
in `test_qdrant_store.py`, `test_pipeline.py`, and new tests for `SemanticRouter`.