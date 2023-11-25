import unittest
from src.algorithms.anagramgentrie import Trie  

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ['apple', 'app', 'apricot', 'banana', 'bat', 'ball']

        for word in self.words:
            self.trie.add(word)

    def test_add(self):
        self.trie.add('application')
        self.assertTrue('application' in self.trie)

    def test_contains(self):
        self.assertTrue('apple' in self.trie)
        self.assertFalse('application' in self.trie)
        self.assertFalse('xyz' in self.trie)

if __name__ == '__main__':
    unittest.main()
