"""
Retriever module for CloudMind RAG pipeline.

Handles semantic search by encoding user queries and retrieving
the most relevant document chunks from the vector store.

Functions:
    retrieve(query: str, k: int) -> List[Document] : Encode query and retrieve k most similar documents.
"""

from typing import List

from src.loaders.base_loader import Document
from src.embeddings.base_embeddings import BaseEmbedder
from src.vectorstores.base_vectorstore import BaseVectorStore


class Retriever:

    def __init__(self, embedder: BaseEmbedder, vectorstore: BaseVectorStore):
        """
        Initialize Retriever with an embedder and a vector store.

        Args:
            embedder (BaseEmbedder): Embedder instance to encode queries.
            vectorstore (BaseVectorStore): Vector store instance to search in.
        """
        self.embedder = embedder
        self.vectorstore = vectorstore

    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """
        Encode the query and retrieve the k most similar documents.

        Args:
            query (str): User question to search for.
            k (int): Number of documents to retrieve. Defaults to 5.

        Returns:
            List[Document]: List of k most relevant documents with similarity scores.
        """
        query_vector = self.embedder.embed_query(query)
        return self.vectorstore.search(query_vector, k=k)