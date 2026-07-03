"""
RAGAS Evaluation script for CloudMind RAG pipeline (Sprint 4 — Part C, step 2).

Scores the generated responses saved by generate_rag_responses.py against
ground_truth.json using RAGAS: Faithfulness, Answer Relevancy, Context Precision
and Context Recall. Results are saved to
backend/results/benchmarks/ragas_evaluation_results.{json,csv}

LLM judge notes:
    qwen3.5:9b (the pipeline's generator model) cannot be used as the RAGAS judge —
    it burns unbounded hidden reasoning tokens even with think=False, so its
    structured-output calls to RAGAS's prompts return empty or time out regardless
    of max_tokens. llama3.2:1b avoids that but is too small to produce schema-valid
    JSON. llama3.1:8b has no hidden thinking overhead and reliably follows RAGAS's
    JSON-based prompts, so it is used here as config.llm.ragas_judge_model.

    RAGAS's modern instructor-based metrics (ragas.metrics.collections, using
    Ollama's OpenAI-compatible /v1 endpoint) hit the same qwen3.5 issue and are
    not used. This script uses RAGAS's legacy LangchainLLMWrapper-based metrics
    instead, which call Ollama's native API (via ChatOllama) and tolerate
    per-row failures through evaluate(..., raise_exceptions=False).

Functions:
    load_generation_output() -> List[dict] : Load generated responses + contexts + references.
    run_ragas_evaluation() -> None : Score all responses with RAGAS and save results.
"""

import json
from pathlib import Path

import torch  # noqa: F401 — import before pandas/pyarrow to avoid a native OpenMP/MKL load-order crash on Windows

from langchain_core.embeddings import Embeddings
from langchain_ollama import ChatOllama
from ragas import evaluate
from ragas.dataset_schema import EvaluationDataset
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms.base import LangchainLLMWrapper
from ragas.metrics import AnswerRelevancy, ContextPrecision, ContextRecall, Faithfulness
from ragas.run_config import RunConfig

from src.embeddings.embedder import Embedder
from src.utils.config import config
from src.utils.settings import settings

GENERATION_OUTPUT_PATH = Path("backend/results/benchmarks/rag_generation_output.json")
EVAL_LIMIT: int | None = 5  # cap queries evaluated; set to None to evaluate all


class _ProjectEmbeddings(Embeddings):
    """Exposes CloudMind's own Embedder (bge-m3, per ADR 003) through LangChain's
    Embeddings interface, so RAGAS's legacy AnswerRelevancy metric (which calls
    embed_query/embed_documents) can use the project's production embedding model
    instead of a separate one."""

    def __init__(self):
        self._embedder = Embedder(model_name=config.embedding.model, use_fp16=config.embedding.use_fp16)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._embedder.model.encode(texts).tolist()

    def embed_query(self, text: str) -> list[float]:
        return self._embedder.embed_query(text).tolist()


def load_generation_output() -> list[dict]:
    """
    Load the generated responses produced by generate_rag_responses.py.

    Returns:
        list[dict]: Entries with 'query', 'response', 'contexts' and 'reference_answer'.

    Raises:
        FileNotFoundError: If the generation output file does not exist.
    """
    if not GENERATION_OUTPUT_PATH.exists():
        raise FileNotFoundError(
            f"Generation output not found: {GENERATION_OUTPUT_PATH}. "
            "Run generate_rag_responses.py first."
        )

    with open(GENERATION_OUTPUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def run_ragas_evaluation() -> None:
    """
    Score generated responses with RAGAS metrics and save results.

    Loads rag_generation_output.json, evaluates each row with Faithfulness,
    Answer Relevancy, Context Precision and Context Recall using llama3.1:8b
    as the LLM judge, and saves per-row and aggregate scores.
    """
    print("CloudMind — RAGAS Evaluation (Part C, step 2)")
    print(f"Judge model : {config.llm.ragas_judge_model}")

    print("\nLoading generation output...")
    data = load_generation_output()
    if EVAL_LIMIT is not None:
        data = data[:EVAL_LIMIT]
    print(f"{len(data)} generated responses loaded")

    rows = [
        {
            "user_input": entry["query"],
            "response": entry["response"],
            "retrieved_contexts": entry["contexts"],
            "reference": entry["reference_answer"],
        }
        for entry in data
    ]
    dataset = EvaluationDataset.from_list(rows)

    base_url = f"http://{settings.ollama_host}:{settings.ollama_port}"
    judge = ChatOllama(
        model=config.llm.ragas_judge_model,
        base_url=base_url,
        num_predict=2048,
        temperature=0,
    )
    llm = LangchainLLMWrapper(judge)
    embeddings = LangchainEmbeddingsWrapper(_ProjectEmbeddings())

    metrics = [Faithfulness(), AnswerRelevancy(), ContextPrecision(), ContextRecall()]

    print("\nScoring responses (sequential, this can take a while)...")
    result = evaluate(
        dataset,
        metrics=metrics,
        llm=llm,
        embeddings=embeddings,
        raise_exceptions=False,
        run_config=RunConfig(max_workers=1, timeout=180, max_retries=2),
    )

    df = result.to_pandas()

    results_path = Path(config.paths.results) / "benchmarks"
    results_path.mkdir(parents=True, exist_ok=True)

    df.to_json(results_path / "ragas_evaluation_results.json", orient="records", indent=2)
    df.to_csv(results_path / "ragas_evaluation_results.csv", index=False)

    print(f"\nResults saved to {results_path}")

    metric_names = [m.name for m in metrics]
    print("\nRAGAS EVALUATION SUMMARY (mean across queries, NaN = failed row)")
    for name in metric_names:
        print(f"{name:<20}: {df[name].mean():.4f}")


if __name__ == "__main__":
    run_ragas_evaluation()
