import pytest
from pathlib import Path


@pytest.fixture
def aws_pdf_dir() -> Path:
    """
    Returns path to AWS PDF test directory.

    Returns:
        Path: Path to backend/data/raw/cloud_docs/aws/
    """
    return Path("backend/data/raw/cloud_docs/aws")


@pytest.fixture
def gcp_md_dir() -> Path:
    """
    Returns path to GCP markdown test directory.

    Returns:
        Path: Path to backend/data/raw/cloud_docs/gcp/
    """
    return Path("backend/data/raw/cloud_docs/gcp")


@pytest.fixture
def finops_csv_path() -> Path:
    """
    Returns path to FinOps CSV test file.

    Returns:
        Path: Path to cloud_budget_2023.csv
    """
    return Path("backend/data/raw/cloud_budget_2023.csv")


@pytest.fixture
def invalid_path() -> Path:
    """
    Returns a non-existent path for negative testing.

    Returns:
        Path: Path that does not exist.
    """
    return Path("backend/data/non_existent_file.pdf")