"""
CSV Loader module 

This module provides the CSVLoader class which handles loading and extracting
text content from CSV files. It supports loading a single CSV file
or an entire directory of CSV files recursively.

Each file is extracted as a single Document with metadata including
the cloud provider (aws, azure, gcp, multicloud) extracted from the file name,
enabling semantic routing in the RAG pipeline.

Functions:
    validate(source_path: str) -> bool : Validate source path exists and contains CSV files.
    load() -> List[Document] : Load all CSV files from source path.
    _load_single_csv(file_path: Path) -> List[Document] : Load a single CSV file.
    _extract_provider(file_path: Path) -> str : Extract cloud provider name from file name.
    _dataframe_to_text(df: pd.DataFrame) -> str : Convert DataFrame to readable text.
"""

from pathlib import Path
from typing import List
import pandas as pd

from src.loaders.base_loader import BaseLoader, Document


class CSVLoader(BaseLoader):

    def __init__(self, source_path: str):
        """
        Initialize CSVLoader.

        Args:
            source_path (str): Path to a CSV file or directory containing CSV files.
        """
        super().__init__(source_path)
        self.path = Path(source_path)

    def validate(self) -> bool:
        """
        Validate that source path exists and contains CSV files.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not self.path.exists():
            return False

        if self.path.is_file():
            return self.path.suffix == ".csv"

        if self.path.is_dir():
            return any(self.path.rglob("*.csv"))

        return False

    def _extract_provider(self, file_path: Path) -> str:
        """
        Extract cloud provider name from file name.

        Args:
            file_path (Path): Path to the CSV file.

        Returns:
            str: Provider name (aws, azure, gcp, multicloud, unknown).
        """
        name = file_path.stem.lower()

        if "aws" in name:
            return "aws"
        elif "azure" in name:
            return "azure"
        elif "gcp" in name:
            return "gcp"
        elif "cloud_budget" in name:
            return "multicloud"

        return "unknown"

    def _dataframe_to_text(self, df: pd.DataFrame) -> str:
        """
        Convert a DataFrame to readable text for RAG.

        Args:
            df (pd.DataFrame): DataFrame to convert.

        Returns:
            str: Human-readable text representation of the DataFrame.
        """
        rows = []
        for _, row in df.iterrows():
            row_text = ", ".join([f"{col}: {val}" for col, val in row.items()])
            rows.append(row_text)
        return "\n".join(rows)

    def _load_single_csv(self, file_path: Path) -> Document:
        """
        Load a single CSV file.

        Args:
            file_path (Path): Path to the CSV file.

        Returns:
            Document: Document with content and metadata.

        Raises:
            ValueError: If the CSV file cannot be read.
        """
        try:
            df = pd.read_csv(file_path)
            content = self._dataframe_to_text(df)

            return Document(
                content=content,
                metadata={
                    "source": str(file_path),
                    "file_name": file_path.name,
                    "provider": self._extract_provider(file_path),
                    "file_type": "csv",
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:
            raise ValueError(f"Failed to load CSV {file_path}: {e}")

    def load(self) -> List[Document]:
        """
        Load all CSV files from source path.

        Returns:
            List[Document]: List of documents with content and metadata.

        Raises:
            ValueError: If source path is invalid.
        """
        if not self.validate():
            raise ValueError(f"Invalid source path: {self.source_path}")

        documents = []

        if self.path.is_file():
            documents.append(self._load_single_csv(self.path))

        elif self.path.is_dir():
            for csv_file in sorted(self.path.rglob("*.csv")):
                documents.append(self._load_single_csv(csv_file))

        return documents