"""
PDF Loader module

This module provides the PDFLoader class which handles loading and extracting
text content from PDF files using PyMuPDF (fitz). It supports loading
a single PDF file or an entire directory of PDFs recursively.

Each page is extracted as a separate Document with rich metadata including
the cloud provider (aws, azure, gcp, compliance) extracted from the file path,
enabling semantic routing in the RAG pipeline.

Functions:
    validate(source_path: str) -> bool : Validate source path exists and contains PDF files.
    load() -> List[Document] : Load all PDF files from source path.
    _load_single_pdf(file_path: Path) -> List[Document] : Load a single PDF file page by page.
    _extract_provider(file_path: Path) -> str : Extract cloud provider name from file path.
"""



from pathlib import Path
from typing import List
import fitz

from src.loaders.base_loader import BaseLoader, Document


class PDFLoader(BaseLoader):

    def __init__(self, source_path: str):
        """
        Initialize PDFLoader.

        Args:
            source_path (str): Path to a PDF file or directory containing PDFs.
        """
        super().__init__(source_path)
        self.path = Path(source_path)

    def validate(self) -> bool:
        """
        Validate that source path exists and contains PDF files.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not self.path.exists():
            return False
        
        if self.path.is_file():
            return self.path.suffix == ".pdf"
        
        if self.path.is_dir():
            return any(self.path.rglob("*.pdf"))
        
        return False

    def load(self) -> List[Document]:
        """
        Load all PDF files from source path.

        Returns:
            List[Document]: List of documents with content and metadata.

        Raises:
            ValueError: If source path is invalid.
        """
        if not self.validate():
            raise ValueError(f"Invalid source path: {self.source_path}")

        documents = []

        if self.path.is_file():
            documents.extend(self._load_single_pdf(self.path))

        elif self.path.is_dir():
            for pdf_file in sorted(self.path.rglob("*.pdf")):
                documents.extend(self._load_single_pdf(pdf_file))

        return documents

    def _load_single_pdf(self, file_path: Path) -> List[Document]:
        """
        Load a single PDF file page by page.

        Args:
            file_path (Path): Path to the PDF file.

        Returns:
            List[Document]: List of documents, one per page.
        
        Raises:
            ValueError: If the PDF file cannot be opened.
        """
        documents = []
        provider = self._extract_provider(file_path)

        try:
            pdf = fitz.open(str(file_path))

            for page_num, page in enumerate(pdf, start=1):
                text = page.get_text()

                if not text.strip():
                    continue

                documents.append(Document(
                    content=text,
                    metadata={
                        "source": str(file_path),
                        "file_name": file_path.name,
                        "provider": provider,
                        "page": page_num,
                        "total_pages": len(pdf),
                        "file_type": "pdf"
                    }
                ))

            pdf.close()

        except Exception as e:
            raise ValueError(f"Failed to load PDF {file_path}: {e}")

        return documents

    def _extract_provider(self, file_path: Path) -> str:
        """
        Extract cloud provider name from file path.

        Args:
            file_path (Path): Path to the PDF file.

        Returns:
            str: Provider name (aws, azure, gcp, compliance, unknown).
        """
        providers = ["aws", "azure", "gcp", "compliance"]
        
        for part in file_path.parts:
            if part.lower() in providers:
                return part.lower()
        
        return "unknown"