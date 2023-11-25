from .ifactory import IAnagramFactory
from readers.urlreader import URLReader

class URLAnagramFactory(IAnagramFactory):
    """Factory for creating URL-based readers and another anagram algorithm."""
    def create_reader(self, url: str) -> URLReader:
        """Creates a URL reader."""
        return URLReader(url)

