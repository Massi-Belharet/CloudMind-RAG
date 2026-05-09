"""
Tests for all document loaders.

"""

import pytest
from pathlib import Path

from src.loaders.pdf_loader import PDFLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.csv_loader import CSVLoader
from src.loaders.base_loader import Document


# PDFLoader 

class TestPDFLoader:

    def test_validate_with_valid_directory(self, aws_pdf_dir):
        loader = PDFLoader(str(aws_pdf_dir))
        assert loader.validate() is True

    def test_validate_with_invalid_path(self, invalid_path):
        loader = PDFLoader(str(invalid_path))
        assert loader.validate() is False

    def test_load_returns_documents(self, aws_pdf_dir):
        loader = PDFLoader(str(aws_pdf_dir))
        docs = loader.load()
        assert len(docs) > 0
        assert all(isinstance(doc, Document) for doc in docs)

    def test_load_documents_have_content(self, aws_pdf_dir):
        loader = PDFLoader(str(aws_pdf_dir))
        docs = loader.load()
        assert all(len(doc.content.strip()) > 0 for doc in docs)

    def test_load_documents_have_correct_metadata(self, aws_pdf_dir):
        loader = PDFLoader(str(aws_pdf_dir))
        docs = loader.load()
        for doc in docs:
            assert doc.metadata["file_type"] == "pdf"
            assert doc.metadata["provider"] == "aws"
            assert "source" in doc.metadata
            assert "file_name" in doc.metadata
            assert "page" in doc.metadata
            assert "total_pages" in doc.metadata

    def test_load_raises_error_on_invalid_path(self, invalid_path):
        loader = PDFLoader(str(invalid_path))
        with pytest.raises(ValueError):
            loader.load()


# MarkdownLoader 

class TestMarkdownLoader:

    def test_validate_with_valid_directory(self, gcp_md_dir):
        loader = MarkdownLoader(str(gcp_md_dir))
        assert loader.validate() is True

    def test_validate_with_invalid_path(self, invalid_path):
        loader = MarkdownLoader(str(invalid_path))
        assert loader.validate() is False

    def test_load_returns_documents(self, gcp_md_dir):
        loader = MarkdownLoader(str(gcp_md_dir))
        docs = loader.load()
        assert len(docs) > 0
        assert all(isinstance(doc, Document) for doc in docs)

    def test_load_documents_have_content(self, gcp_md_dir):
        loader = MarkdownLoader(str(gcp_md_dir))
        docs = loader.load()
        assert all(len(doc.content.strip()) > 0 for doc in docs)

    def test_load_documents_have_correct_metadata(self, gcp_md_dir):
        loader = MarkdownLoader(str(gcp_md_dir))
        docs = loader.load()
        for doc in docs:
            assert doc.metadata["file_type"] == "markdown"
            assert doc.metadata["provider"] == "gcp"
            assert "source" in doc.metadata
            assert "file_name" in doc.metadata

    def test_load_raises_error_on_invalid_path(self, invalid_path):
        loader = MarkdownLoader(str(invalid_path))
        with pytest.raises(ValueError):
            loader.load()


# CSVLoader 

class TestCSVLoader:

    def test_validate_with_valid_file(self, finops_csv_path):
        loader = CSVLoader(str(finops_csv_path))
        assert loader.validate() is True

    def test_validate_with_invalid_path(self, invalid_path):
        loader = CSVLoader(str(invalid_path))
        assert loader.validate() is False

    def test_load_returns_documents(self, finops_csv_path):
        loader = CSVLoader(str(finops_csv_path))
        docs = loader.load()
        assert len(docs) > 0
        assert all(isinstance(doc, Document) for doc in docs)

    def test_load_documents_have_content(self, finops_csv_path):
        loader = CSVLoader(str(finops_csv_path))
        docs = loader.load()
        assert all(len(doc.content.strip()) > 0 for doc in docs)

    def test_load_documents_have_correct_metadata(self, finops_csv_path):
        loader = CSVLoader(str(finops_csv_path))
        docs = loader.load()
        for doc in docs:
            assert doc.metadata["file_type"] == "csv"
            assert doc.metadata["provider"] == "multicloud"
            assert "source" in doc.metadata
            assert "file_name" in doc.metadata
            assert "rows" in doc.metadata
            assert "columns" in doc.metadata

    def test_load_raises_error_on_invalid_path(self, invalid_path):
        loader = CSVLoader(str(invalid_path))
        with pytest.raises(ValueError):
            loader.load()

    def test_dataframe_to_text_format(self, finops_csv_path):
        import pandas as pd
        loader = CSVLoader(str(finops_csv_path))
        df = pd.DataFrame({"col1": ["val1"], "col2": ["val2"]})
        text = loader._dataframe_to_text(df)
        assert "col1: val1" in text
        assert "col2: val2" in text