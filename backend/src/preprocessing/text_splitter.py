"""
Text Splitter module 

Handles splitting of documents into chunks based on their file type.
PDF documents are split using RecursiveCharacterTextSplitter, Markdown
documents are split by headers first then by size if needed, and CSV
documents are split by lines to keep rows intact.

Functions:
    split(documents: List[Document]) -> List[Document] : Split a list of documents into chunks based on file type.
    _split_text(document: Document) -> List[Document] : Split a PDF document using RecursiveCharacterTextSplitter.
    _split_markdown(document: Document) -> List[Document] : Split a Markdown document by headers then by size.
    _split_csv(document: Document) -> List[Document] : Split a CSV document by lines.
"""




from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter


from src.loaders.base_loader import Document


class TextSplitter:

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50, csv_chunk_size: int = 100):
        """
        Initialize TextSplitter with chunk size and overlap.

        Args:
            chunk_size (int): Maximum size of each chunk in characters.
            chunk_overlap (int): Number of overlapping characters between chunks.
            csv_chunk_size (int): Number of rows per chunk for CSV files.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.csv_chunk_size = csv_chunk_size

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "section"),
                ("##", "subsection"),
                ("###", "subsubsection")
            ]
        )

    def split(self, documents: List[Document]) -> List[Document]:
        """
        Split a list of documents into chunks based on their file type.

        Args:
            documents (List[Document]): List of documents to split.

        Returns:
            List[Document]: List of chunked documents.
        """
        chunked_documents = []

        for document in documents:
            file_type = document.metadata.get("file_type")

            if file_type == "csv":
                chunked_documents.extend(self._split_csv(document))
            elif file_type == "markdown":
                chunked_documents.extend(self._split_markdown(document))
            else:
                chunked_documents.extend(self._split_text(document))

        return chunked_documents

    def _split_text(self, document: Document) -> List[Document]:
        """
        Split a PDF document into chunks using RecursiveCharacterTextSplitter.

        Args:
            document (Document): Document to split.

        Returns:
            List[Document]: List of chunked documents with updated metadata.
        """
        chunks = self.text_splitter.split_text(document.content)

        return [
            Document(
                content=chunk,
                metadata={
                    **document.metadata,
                    "chunk_index": i,
                    "chunk_total": len(chunks)
                }
            )
            for i, chunk in enumerate(chunks)
        ]

    def _split_markdown(self, document: Document) -> List[Document]:
        """
        Split a Markdown document by headers first, then by size if needed.

        Args:
            document (Document): Markdown document to split.

        Returns:
            List[Document]: List of chunked documents with section metadata.
        """
        # Step 1 — split by headers
        md_chunks = self.markdown_splitter.split_text(document.content)
        documents = []

        for i, chunk in enumerate(md_chunks):
            metadata = {
                **document.metadata,
                "chunk_index": i,
                "chunk_total": len(md_chunks)
            }

            if "section" in chunk.metadata:
                metadata["section"] = chunk.metadata["section"]
            if "subsection" in chunk.metadata:
                metadata["subsection"] = chunk.metadata["subsection"]

            # Step 2 — if chunk still too large, split by size
            if len(chunk.page_content) > self.chunk_size:
                sub_chunks = self.text_splitter.split_text(chunk.page_content)
                for j, sub_chunk in enumerate(sub_chunks):
                    documents.append(Document(
                        content=sub_chunk,
                        metadata={
                            **metadata,
                            "chunk_index": f"{i}.{j}",
                            "chunk_total": len(md_chunks)
                        }
                    ))
            else:
                documents.append(Document(
                    content=chunk.page_content,
                    metadata=metadata
                ))

        return documents

    def _split_csv(self, document: Document) -> List[Document]:
        """
        Split a CSV document into chunks by number of rows to keep rows intact.

        Args:
            document (Document): CSV document to split.

        Returns:
            List[Document]: List of chunked documents with updated metadata.
        """
        lines = document.content.strip().split("\n")
        chunks = [
            "\n".join(lines[i:i + self.csv_chunk_size])
            for i in range(0, len(lines), self.csv_chunk_size)
        ]

        return [
            Document(
                content=chunk,
                metadata={
                    **document.metadata,
                    "chunk_index": i,
                    "chunk_total": len(chunks)
                }
            )
            for i, chunk in enumerate(chunks)
        ]