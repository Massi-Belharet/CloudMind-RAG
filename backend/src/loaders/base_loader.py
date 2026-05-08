from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Document:
    """
    Represents a loaded document with content and metadata.
    
    Attributes:
        content (str): The text content of the document.
        metadata (dict): Additional information about the document.
    """
    content: str
    metadata: dict


class BaseLoader(ABC):
    """
    Abstract base class for all document loaders.
    """

    def __init__(self, source_path: str):
        """
        Initialize the loader with a source path.

        Args:
            source_path (str): Path to the file or directory to load.
        """
        self.source_path = source_path

    @abstractmethod
    def load(self) -> List[Document]:
        """
        Load documents from source.

        Returns:
            List[Document]: List of loaded documents with metadata.
        """
        pass

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate that the source exists and is readable.

        Returns:
            bool: True if source is valid, False otherwise.
        """
        pass