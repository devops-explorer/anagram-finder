from src.readers.urlreader import URLReader
import unittest

class TestURLReader(unittest.TestCase):
    def test_url_fetch(self):
        url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
        reader = URLReader(url)
        data = reader.read()
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()
