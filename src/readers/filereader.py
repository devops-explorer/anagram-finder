from .ireader  import IReader
from typing import List
import logging

class FileReader(IReader):
    """Reads words from a local file."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> List[str]:
        """Reads words from a file and returns a list of words."""
        try:
            with open(self.file_path, 'r') as file:
                return [line.strip() for line in file]
        except FileNotFoundError as e:
            logging.error(f"File not found: {self.file_path}")
            raise e
