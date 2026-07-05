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
    _remove_related_links_boilerplate(text: str) -> str : Remove Microsoft Learn "related links" footer noise.
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
        text = self._remove_related_links_boilerplate(text)

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
        text = re.sub(r'^\s*\d+\s*/\s*\d+\s*$', '', text, flags=re.MULTILINE)
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

    def _remove_related_links_boilerplate(self, text: str) -> str:
        """
        Remove Microsoft Learn "related links" footer noise.

        Azure Well-Architected Framework / Architecture Center pages end with
        a block of bare, unexplained link titles (often "What is X?" phrasing),
        anchored by "Refer to the complete set of recommendations." and/or
        "Last updated on <date>", followed by a "Next steps"/"Related links"
        pointer and the linked article title repeated once or twice. Unlike
        genuine bulleted content (e.g. a recommendations checklist), these
        lines carry no explanatory sentence of their own, which is the signal
        used here instead of "is it a list". Confirmed via direct PDF
        inspection to be specific to Microsoft Learn documents (absent from
        the AWS/GCP/compliance sources in this corpus).
        """
        lines = text.split("\n")
        n = len(lines)
        remove = [False] * n

        refer_re = re.compile(r'^\s*Refer to the complete set of recommendations\.\s*$', re.IGNORECASE)
        last_updated_re = re.compile(r'^\s*Last updated on\s+\d{1,2}/\d{1,2}/\d{4}\s*$', re.IGNORECASE)
        nav_header_re = re.compile(r'^\s*(Next steps|Related links|Related resources|Community links)\s*$', re.IGNORECASE)
        timestamp_re = re.compile(r'^\s*\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}\s*$')
        ms_learn_title_re = re.compile(r'^.*\|\s*Microsoft Learn\s*$')
        url_re = re.compile(r'^\s*https?://\S+\s*$')

        def is_sentence(candidate: str) -> bool:
            return candidate.endswith(".") and len(candidate.split()) > 12

        def is_boundary(candidate: str) -> bool:
            # A separate boilerplate marker means we've crossed into another
            # page-footer block entirely - stop rather than eat through it.
            return bool(
                timestamp_re.match(candidate)
                or ms_learn_title_re.match(candidate)
                or url_re.match(candidate)
                or refer_re.match(candidate)
                or last_updated_re.match(candidate)
            )

        def consume_backward(idx: int, max_lines: int = 15) -> None:
            j = idx - 1
            consumed = 0
            while j >= 0 and consumed < max_lines:
                candidate = lines[j].strip()
                if not candidate or len(candidate) > 100 or is_sentence(candidate) or is_boundary(candidate):
                    break
                remove[j] = True
                j -= 1
                consumed += 1

        def consume_forward(idx: int, max_lines: int = 6) -> None:
            j = idx + 1
            consumed = 0
            while j < n and consumed < max_lines:
                candidate = lines[j].strip()
                if not candidate or len(candidate) > 100 or is_sentence(candidate) or is_boundary(candidate):
                    break
                remove[j] = True
                j += 1
                consumed += 1

        for i, raw_line in enumerate(lines):
            line = raw_line.strip()
            if refer_re.match(line):
                remove[i] = True
                consume_backward(i)
            elif last_updated_re.match(line):
                remove[i] = True
                consume_backward(i)
                consume_forward(i)
            elif nav_header_re.match(line):
                remove[i] = True
                consume_backward(i)
            elif timestamp_re.match(line) or ms_learn_title_re.match(line) or url_re.match(line):
                remove[i] = True

        cleaned_lines = [raw for i, raw in enumerate(lines) if not remove[i]]
        text = "\n".join(cleaned_lines)
        text = re.sub(r'\n{3,}', '\n\n', text).strip()
        return text