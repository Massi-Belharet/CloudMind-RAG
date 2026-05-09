"""
Markdown Loader module

This module provides the MarkdownLoader class which handles loading and extracting
text content from Markdown files. It supports loading a single markdown file
or an entire directory of markdown files recursively.

Each file is extracted as a single Document with metadata including
the cloud provider (aws, azure, gcp, compliance) extracted from the file path,
enabling semantic routing in the RAG pipeline.

Functions:
    validate(source_path: str) -> bool : Validate source path exists and contains markdown files.
    load() -> List[Document] : Load all markdown files from source path.
    _load_single_markdown(file_path: Path) -> Document : Load a single markdown file.
    _extract_provider(file_path: Path) -> str : Extract cloud provider name from file path.
"""




from pathlib import Path
from typing import List

from src.loaders.base_loader import BaseLoader, Document


class MarkdownLoader(BaseLoader):

    def __init__(self, source_path: str):
        """
        Initialize MarkdownLoader.

        Args:
            source_path (str): Path to a markdown file or directory containing markdown files.
        """
        super().__init__(source_path)
        self.path = Path(source_path)

    def validate(self) -> bool:
        """
        Validate that source path exists and contains markdown files.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not self.path.exists():
            return False

        if self.path.is_file():
            return self.path.suffix == ".md"

        if self.path.is_dir():
            return any(self.path.rglob("*.md"))

        return False

    def load(self) -> List[Document]:
        """
        Load all markdown files from source path.

        Returns:
            List[Document]: List of documents with content and metadata.

        Raises:
            ValueError: If source path is invalid.
        """
        if not self.validate():
            raise ValueError(f"Invalid source path: {self.source_path}")

        documents = []

        if self.path.is_file():
            documents.append(self._load_single_markdown(self.path))

        elif self.path.is_dir():
            for md_file in sorted(self.path.rglob("*.md")):
                documents.append(self._load_single_markdown(md_file))

        return documents

    def _load_single_markdown(self, file_path: Path) -> Document:
        """
        Load a single markdown file.

        Args:
            file_path (Path): Path to the markdown file.

        Returns:
            Document: Document with content and metadata.

        Raises:
            ValueError: If the markdown file cannot be read.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            return Document(
                content=content,
                metadata={
                    "source": str(file_path),
                    "file_name": file_path.name,
                    "provider": self._extract_provider(file_path),
                    "file_type": "markdown"
                }
            )

        except Exception as e:
            raise ValueError(f"Failed to load markdown {file_path}: {e}")

    def _extract_provider(self, file_path: Path) -> str:
        """
        Extract cloud provider name from file path.

        Args:
            file_path (Path): Path to the markdown file.

        Returns:
            str: Provider name (aws, azure, gcp, compliance, unknown).
        """
        providers = ["aws", "azure", "gcp", "compliance"]

        for part in file_path.parts:
            if part.lower() in providers:
                return part.lower()

        return "unknown"