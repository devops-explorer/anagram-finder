import requests
from .ireader import IReader

class URLReader(IReader):
    def __init__(self, path: str):
        self.path = path

    def read(self):
        response = requests.get(self.path)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            return []
