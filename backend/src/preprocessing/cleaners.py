"""
Text Cleaner module 

Handles cleaning of raw text extracted from documents before splitting.
CSV documents are skipped as they don't require text cleaning.
PDF and Markdown documents go through page number removal, special
character cleaning, and whitespace normalization.

Functions:
    clean(documents: List[Document]) -> List[Document] : Clean a list of documents based on file type.
    _clean_document(document: Document) -> Document : Apply all cleaning steps to a single document.
    _remove_extra_whitespace(text: str) -> str : Normalize multiple spaces and excessive newlines.
    _remove_page_numbers(text: str) -> str : Remove common page number patterns from PDF text.
    _remove_special_characters(text: str) -> str : Remove non-printable and unwanted special characters.
"""



import re
from typing import List

from src.loaders.base_loader import Document


class TextCleaner:

    def clean(self, documents: List[Document]) -> List[Document]:
        """
        Clean a list of documents based on their file type.

        Args:
            documents (List[Document]): List of documents to clean.

        Returns:
            List[Document]: List of cleaned documents.
        """
        cleaned = []

        for document in documents:
            if document.metadata.get("file_type") == "csv":
                cleaned.append(document)
            else:
                cleaned_doc = self._clean_document(document)
                if cleaned_doc.content.strip():
                    cleaned.append(cleaned_doc)

        return cleaned

    def _clean_document(self, document: Document) -> Document:
        """
        Apply all cleaning steps to a single document.

        Args:
            document (Document): Document to clean.

        Returns:
            Document: Cleaned document with same metadata.
        """
        text = document.content
        text = self._remove_page_numbers(text)
        text = self._remove_special_characters(text)
        text = self._remove_extra_whitespace(text)

        return Document(
            content=text,
            metadata=document.metadata
        )

    def _remove_extra_whitespace(self, text: str) -> str:
        """
        Normalize multiple spaces and excessive newlines.

        Args:
            text (str): Raw text to clean.

        Returns:
            str: Text with normalized whitespace.
        """
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def _remove_page_numbers(self, text: str) -> str:
        """
        Remove common page number patterns from extracted PDF text.

        Args:
            text (str): Raw text to clean.

        Returns:
            str: Text without page number patterns.
        """
        text = re.sub(r'Page \d+ of \d+', '', text, flags=re.IGNORECASE)
        text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)
        return text

    def _remove_special_characters(self, text: str) -> str:
        """
        Remove non-printable and unwanted special characters.

        Args:
            text (str): Raw text to clean.

        Returns:
            str: Text with special characters removed.
        """
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
        text = re.sub(r'[^\x00-\x7F\u00C0-\u024F\u2000-\u206F]', ' ', text)
        return text