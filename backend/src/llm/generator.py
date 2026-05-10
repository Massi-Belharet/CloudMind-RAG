"""
Generator module 

Implements BaseLLM using to generate responses
based on retrieved documents and user queries. Builds a structured
context from Document chunks and uses the CloudMind RAG prompt
to ensure grounded, hallucination-free responses.

Functions:
    generate(query: str, documents: List[Document]) -> str : Generate a response from query and retrieved documents.
"""

from typing import List

from src.loaders.base_loader import Document
from src.llm.base import BaseLLM
from src.llm.prompts import get_rag_prompt


class Generator(BaseLLM):

    def generate(self, query: str, documents: List[Document]) -> str:
        """
        Generate a response based on the query and retrieved documents.

        Args:
            query (str): User question to answer.
            documents (List[Document]): Retrieved documents to use as context.

        Returns:
            str: Generated response from the LLM.
        """
        context = self._build_context(documents)
        prompt = get_rag_prompt()
        chain = prompt | self.llm
        response = chain.invoke({"context": context, "question": query})
        return response.content

    def _build_context(self, documents: List[Document]) -> str:
        """
        Build a structured context string from retrieved documents.

        Args:
            documents (List[Document]): List of retrieved documents.

        Returns:
            str: Formatted context string with provider and content.
        """
        context_parts = []

        for i, doc in enumerate(documents, start=1):
            provider = doc.metadata.get("provider", "unknown").upper()
            source = doc.metadata.get("file_name", "unknown")
            context_parts.append(
                f"[{i}] Source: {provider} — {source}\n{doc.content}"
            )

        return "\n\n".join(context_parts)