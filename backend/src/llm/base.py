"""
Base LLM module 

Defines the abstract interface that all LLM implementations must follow.
Uses LangChain BaseChatModel for dependency injection, making it easy
to swap between Ollama, OpenAI, or any other LangChain-compatible model
without changing the pipeline code.

Functions:
    generate(query: str, documents: List[Document]) -> str : Generate a response from query and retrieved documents.
"""

from abc import ABC, abstractmethod
from typing import List

from langchain_core.language_models import BaseChatModel

from src.loaders.base_loader import Document


class BaseLLM(ABC):

    def __init__(self, llm: BaseChatModel):
        """
        Initialize with any LangChain-compatible chat model.

        Args:
            llm (BaseChatModel): LangChain chat model instance.
        """
        self.llm = llm

    @abstractmethod
    def generate(self, query: str, documents: List[Document]) -> str:
        """
        Generate a response based on the query and retrieved documents.

        Args:
            query (str): User question to answer.
            documents (List[Document]): Retrieved documents to use as context.

        Returns:
            str: Generated response from the LLM.
        """
        pass