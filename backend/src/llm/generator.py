"""
Generator module

Implements BaseLLM using to generate responses
based on retrieved documents and user queries. Builds a structured
context from Document chunks and uses the CloudMind RAG prompt
to ensure grounded, hallucination-free responses.

Functions:
    generate(query: str, documents: List[Document]) -> str : Generate a response from query and retrieved documents.
    generate_stream(query: str, documents: List[Document]) -> Iterator[str] : Stream a response fragment by fragment.
"""

from typing import Iterator, List

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

    def generate_stream(self, query: str, documents: List[Document]) -> Iterator[str]:
        """
        Generate a response as a stream of text fragments based on the query
        and retrieved documents. Uses the same prompt and context construction
        as generate(), but yields fragments as they arrive from the LLM instead
        of waiting for the full response.

        Args:
            query (str): User question to answer.
            documents (List[Document]): Retrieved documents to use as context.

        Yields:
            str: Successive text fragments of the generated response.
        """
        context = self._build_context(documents)
        prompt = get_rag_prompt()
        chain = prompt | self.llm
        for chunk in chain.stream({"context": context, "question": query}):
            if chunk.content:
                yield chunk.content

    def _build_context(self, documents: List[Document]) -> str:
        """
        Build a context string from retrieved documents.

        Args:
            documents (List[Document]): List of retrieved documents.

        Returns:
            str: Concatenated document contents, with no source labels or
            numbering. Earlier versions prefixed each chunk with "[i] Source:
            PROVIDER — file_name", which the LLM would imitate in its answers
            — sometimes as bracketed reference numbers, sometimes as markdown
            links to the file name, which is never a real URL and renders as
            a broken/dead link in the UI.
        """
        return "\n\n".join(doc.content for doc in documents)