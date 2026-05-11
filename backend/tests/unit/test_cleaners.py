"""
Tests for TextCleaner module 

Covers clean(), _clean_document(), _remove_extra_whitespace(),
_remove_page_numbers(), and _remove_special_characters().
"""

import pytest
from src.loaders.base_loader import Document
from src.preprocessing.cleaners import TextCleaner


#  Fixtures 

@pytest.fixture
def cleaner():
    return TextCleaner()


@pytest.fixture
def pdf_document():
    return Document(
        content="AWS recommends using multiple zones.\n\n\n\n"
                "Page 1 of 10\n"
                "This ensures high availability.\n"
                "Page 2 of 10\n\n"
                "Cost optimization is key.",
        metadata={
            "file_name": "aws-overview.pdf",
            "provider": "aws",
            "file_type": "pdf"
        }
    )


@pytest.fixture
def markdown_document():
    return Document(
        content="# Cost Optimization\n\n\n"
                "Reduce unnecessary expenses.\n\n"
                "## Right-sizing\n\n"
                "Choose the right instance type.",
        metadata={
            "file_name": "cost_optimization.md",
            "provider": "gcp",
            "file_type": "markdown"
        }
    )


@pytest.fixture
def csv_document():
    return Document(
        content="date: 2023-01-01, provider: AWS, cost: 1250.00\n"
                "date: 2023-01-02, provider: Azure, cost: 890.00",
        metadata={
            "file_name": "cloud_budget_2023.csv",
            "provider": "multicloud",
            "file_type": "csv"
        }
    )


@pytest.fixture
def empty_document():
    return Document(
        content="   \n\n   ",
        metadata={
            "file_name": "empty.pdf",
            "provider": "aws",
            "file_type": "pdf"
        }
    )


#  TextCleaner.clean() 

class TestClean:

    def test_clean_returns_documents(self, cleaner, pdf_document):
        docs = cleaner.clean([pdf_document])
        assert len(docs) > 0
        assert all(isinstance(d, Document) for d in docs)

    def test_clean_skips_csv(self, cleaner, csv_document):
        docs = cleaner.clean([csv_document])
        assert docs[0].content == csv_document.content

    def test_clean_removes_empty_documents(self, cleaner, empty_document):
        docs = cleaner.clean([empty_document])
        assert len(docs) == 0

    def test_clean_preserves_metadata(self, cleaner, pdf_document):
        docs = cleaner.clean([pdf_document])
        assert docs[0].metadata["provider"] == "aws"
        assert docs[0].metadata["file_type"] == "pdf"

    def test_clean_multiple_documents(self, cleaner, pdf_document, markdown_document, csv_document):
        docs = cleaner.clean([pdf_document, markdown_document, csv_document])
        assert len(docs) == 3


# TextCleaner._remove_page_numbers() 

class TestRemovePageNumbers:

    def test_removes_page_x_of_y(self, cleaner):
        text = "Some content\nPage 3 of 10\nMore content"
        result = cleaner._remove_page_numbers(text)
        assert "Page 3 of 10" not in result

    def test_removes_standalone_numbers(self, cleaner):
        text = "Some content\n42\nMore content"
        result = cleaner._remove_page_numbers(text)
        assert "\n42\n" not in result

    def test_preserves_content(self, cleaner):
        text = "AWS recommends high availability.\nPage 1 of 5\nUse multiple zones."
        result = cleaner._remove_page_numbers(text)
        assert "AWS recommends high availability." in result
        assert "Use multiple zones." in result


# TextCleaner._remove_extra_whitespace() 

class TestRemoveExtraWhitespace:

    def test_normalizes_multiple_spaces(self, cleaner):
        text = "AWS    recommends    high    availability"
        result = cleaner._remove_extra_whitespace(text)
        assert "  " not in result

    def test_normalizes_excessive_newlines(self, cleaner):
        text = "First paragraph\n\n\n\n\nSecond paragraph"
        result = cleaner._remove_extra_whitespace(text)
        assert "\n\n\n" not in result

    def test_strips_leading_trailing_whitespace(self, cleaner):
        text = "   AWS recommends high availability.   "
        result = cleaner._remove_extra_whitespace(text)
        assert result == result.strip()


# TextCleaner._remove_special_characters() 

class TestRemoveSpecialCharacters:

    def test_removes_non_printable_characters(self, cleaner):
        text = "AWS\x00recommends\x1fhigh availability"
        result = cleaner._remove_special_characters(text)
        assert "\x00" not in result
        assert "\x1f" not in result

    def test_preserves_french_accents(self, cleaner):
        text = "Résilience, accès et disponibilité sont essentielles."
        result = cleaner._remove_special_characters(text)
        assert "é" in result
        assert "è" in result

    def test_preserves_normal_content(self, cleaner):
        text = "AWS recommends using S3 for storage."
        result = cleaner._remove_special_characters(text)
        assert "AWS recommends using S3 for storage." in result