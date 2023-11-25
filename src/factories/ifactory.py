from abc import ABC, abstractmethod

class IAnagramFactory(ABC):
    """Interface defining methods to create readers and anagram algorithms."""

    @abstractmethod
    def create_reader(self, source: str):
        """Abstract method to create a reader based on source."""
        pass

