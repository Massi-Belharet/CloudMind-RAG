"""
Multi-Query Retriever module

Implements RAG-Fusion: generates multiple semantically distinct reformulations
of the user's query using an LLM, retrieves documents for the original query
and each reformulation via HybridRetriever, and fuses all result lists using
Reciprocal Rank Fusion.

Functions:
    retrieve(query: str, k: int, filter_provider: Optional[str]) -> List[Document] : Retrieve top-k documents using multi-query RAG-Fusion, optionally restricted to one provider.
"""

from typing import List, Optional

from langchain_core.language_models import BaseChatModel

from src.loaders.base_loader import Document
from src.rag.hybrid_retriever import HybridRetriever
from src.rag.fusion import rrf_fusion
from src.llm.prompts import get_multi_query_prompt
from src.utils.config import config


class MultiQueryRetriever:

    def __init__(self, llm: BaseChatModel, retriever: HybridRetriever, n_queries: int = None, rrf_k: int = 60):
        """
        Initialize MultiQueryRetriever with an LLM for query generation and a hybrid retriever.

        Args:
            llm (BaseChatModel): Chat model used to generate query reformulations.
            retriever (HybridRetriever): Hybrid retriever used for the original query and each reformulation.
            n_queries (int): Number of reformulations to generate. Defaults to config value.
            rrf_k (int): RRF smoothing constant for fusing results across query variants. Defaults to 60.
        """
        self.llm = llm
        self.retriever = retriever
        self.n_queries = n_queries or config.multi_query.n_queries
        self.rrf_k = rrf_k
        self.prompt = get_multi_query_prompt(n_queries=self.n_queries)
        self.chain = self.prompt | self.llm

    def _generate_queries(self, query: str) -> List[str]:
        """
        Generate semantically distinct reformulations of the query using the LLM.

        Args:
            query (str): Original user question.

        Returns:
            List[str]: Reformulated queries (does not include the original question).
        """
        response = self.chain.invoke({"question": query})
        content = response.content.strip()

        if "</think>" in content:
            content = content.split("</think>")[-1].strip()

        if not content:
            content = response.additional_kwargs.get("thinking", "").strip()

        lines = content.split("\n")
        reformulations = [line.strip() for line in lines if line.strip()]
        return reformulations[:self.n_queries]

    def retrieve(self, query: str, k: int = 5, filter_provider: Optional[str] = None) -> List[Document]:
        """
        Retrieve top-k documents using RAG-Fusion.

        The original query and its LLM-generated reformulations are each searched
        via HybridRetriever, and the resulting ranked lists are fused with RRF.

        Args:
            query (str): User question to search for.
            k (int): Number of documents to retrieve. Defaults to 5.
            filter_provider (Optional[str]): If set, restrict results to this provider.
                Applied identically to the original query and every reformulation
                (the provider should be detected once, upstream, on the original
                query only — not re-detected per reformulation). Defaults to None,
                which searches across all providers (unchanged behavior).

        Returns:
            List[Document]: Top-k most relevant documents after RRF fusion across all query variants.
        """
        reformulations = self._generate_queries(query)
        all_queries = [query] + reformulations

        ranked_lists = [
            self.retriever.retrieve(q, k=k * 2, filter_provider=filter_provider) for q in all_queries
        ]

        return rrf_fusion(ranked_lists=ranked_lists, k=k, rrf_k=self.rrf_k)