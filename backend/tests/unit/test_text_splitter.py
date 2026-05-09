"""
Tests for TextSplitter module 

"""

import pytest
from src.loaders.base_loader import Document
from src.preprocessing.text_splitter import TextSplitter


#  Fixtures 

@pytest.fixture
def pdf_document():
    return Document(
        content="AWS recommends using multiple availability zones.\n\n"
                "This ensures high availability for your applications.\n\n"
                "Cost optimization is a key pillar of the Well-Architected Framework.\n\n"
                "Security must be considered at every layer of your architecture.",
        metadata={
            "source": "backend/data/raw/cloud_docs/aws/aws-overview.pdf",
            "file_name": "aws-overview.pdf",
            "provider": "aws",
            "file_type": "pdf",
            "page": 1,
            "total_pages": 10
        }
    )


@pytest.fixture
def markdown_document():
    return Document(
        content="# Cost Optimization\n\n"
                "Cost optimization is about reducing unnecessary expenses.\n\n"
                "## Right-sizing\n\n"
                "Choose the right instance type for your workload.\n\n"
                "## Reserved Instances\n\n"
                "Save up to 72% compared to on-demand pricing.",
        metadata={
            "source": "backend/data/raw/cloud_docs/gcp/Cost_optimization_pillar.md",
            "file_name": "Cost_optimization_pillar.md",
            "provider": "gcp",
            "file_type": "markdown"
        }
    )


@pytest.fixture
def csv_document():
    lines = "\n".join([
        f"date: 2023-01-{i:02d}, provider: AWS, cost: {100 + i}.00"
        for i in range(1, 250)
    ])
    return Document(
        content=lines,
        metadata={
            "source": "backend/data/raw/cloud_budget_2023.csv",
            "file_name": "cloud_budget_2023.csv",
            "provider": "multicloud",
            "file_type": "csv",
            "rows": 249
        }
    )


@pytest.fixture
def splitter():
    return TextSplitter(chunk_size=200, chunk_overlap=20, csv_chunk_size=100)


#  TextSplitter.split() 

class TestSplit:

    def test_split_returns_documents(self, splitter, pdf_document):
        chunks = splitter.split([pdf_document])
        assert len(chunks) > 0
        assert all(isinstance(c, Document) for c in chunks)

    def test_split_multiple_documents(self, splitter, pdf_document, markdown_document, csv_document):
        chunks = splitter.split([pdf_document, markdown_document, csv_document])
        assert len(chunks) > 0

    def test_split_empty_list(self, splitter):
        chunks = splitter.split([])
        assert chunks == []


#  TextSplitter._split_text() 

class TestSplitText:

    def test_pdf_chunks_have_content(self, splitter, pdf_document):
        chunks = splitter._split_text(pdf_document)
        assert all(len(c.content.strip()) > 0 for c in chunks)

    def test_pdf_chunks_preserve_metadata(self, splitter, pdf_document):
        chunks = splitter._split_text(pdf_document)
        for chunk in chunks:
            assert chunk.metadata["provider"] == "aws"
            assert chunk.metadata["file_type"] == "pdf"
            assert chunk.metadata["file_name"] == "aws-overview.pdf"

    def test_pdf_chunks_have_chunk_metadata(self, splitter, pdf_document):
        chunks = splitter._split_text(pdf_document)
        for chunk in chunks:
            assert "chunk_index" in chunk.metadata
            assert "chunk_total" in chunk.metadata

    def test_pdf_chunks_respect_chunk_size(self, splitter, pdf_document):
        chunks = splitter._split_text(pdf_document)
        assert all(len(c.content) <= splitter.chunk_size * 1.1 for c in chunks)


#  TextSplitter._split_markdown() 

class TestSplitMarkdown:

    def test_markdown_chunks_have_content(self, splitter, markdown_document):
        chunks = splitter._split_markdown(markdown_document)
        assert all(len(c.content.strip()) > 0 for c in chunks)

    def test_markdown_chunks_preserve_metadata(self, splitter, markdown_document):
        chunks = splitter._split_markdown(markdown_document)
        for chunk in chunks:
            assert chunk.metadata["provider"] == "gcp"
            assert chunk.metadata["file_type"] == "markdown"

    def test_markdown_chunks_have_section_metadata(self, splitter, markdown_document):
        chunks = splitter._split_markdown(markdown_document)
        assert any("section" in c.metadata for c in chunks)

    def test_markdown_chunks_have_chunk_metadata(self, splitter, markdown_document):
        chunks = splitter._split_markdown(markdown_document)
        for chunk in chunks:
            assert "chunk_index" in chunk.metadata
            assert "chunk_total" in chunk.metadata


# TextSplitter._split_csv() 

class TestSplitCSV:

    def test_csv_chunks_have_content(self, splitter, csv_document):
        chunks = splitter._split_csv(csv_document)
        assert all(len(c.content.strip()) > 0 for c in chunks)

    def test_csv_chunks_respect_row_size(self, splitter, csv_document):
        chunks = splitter._split_csv(csv_document)
        for chunk in chunks:
            lines = chunk.content.strip().split("\n")
            assert len(lines) <= splitter.csv_chunk_size

    def test_csv_chunks_preserve_metadata(self, splitter, csv_document):
        chunks = splitter._split_csv(csv_document)
        for chunk in chunks:
            assert chunk.metadata["provider"] == "multicloud"
            assert chunk.metadata["file_type"] == "csv"

    def test_csv_chunks_have_chunk_metadata(self, splitter, csv_document):
        chunks = splitter._split_csv(csv_document)
        for chunk in chunks:
            assert "chunk_index" in chunk.metadata
            assert "chunk_total" in chunk.metadata

    def test_csv_249_rows_produces_3_chunks(self, splitter, csv_document):
        chunks = splitter._split_csv(csv_document)
        assert len(chunks) == 3