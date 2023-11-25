from .ifactory import IAnagramFactory
from readers.filereader import FileReader

class FileAnagramFactory(IAnagramFactory):
    """Factory for creating file-based readers and character count anagram algorithm."""

    def create_reader(self, file_path: str):
        """Creates a file reader."""
        return FileReader(file_path)

