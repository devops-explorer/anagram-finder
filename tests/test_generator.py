import unittest
from src.algorithms.anagramgentrie import Trie, TrieAnagramStrategy

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

class TestAnagramGenerator(unittest.TestCase):

    def setUp(self):
        self.corpus = ['listen', 'silent', 'enlist', 'banana', 'bat', 'ball']
        self.anagram_generator = TrieAnagramStrategy(self.corpus)

    def test_generate(self):
        anagrams_listen = self.anagram_generator.generate('listen')
        self.assertEqual(len(anagrams_listen), 3)  # Expect three anagrams: listen, silent, enlist
        self.assertIn(['listen'], anagrams_listen)
        self.assertIn(['silent'], anagrams_listen)
        self.assertIn(['enlist'], anagrams_listen)

        anagrams_bat = self.anagram_generator.generate('bat')
        self.assertEqual(len(anagrams_bat), 1)  # Expect one anagram: bat
        self.assertIn(['bat'], anagrams_bat)

        anagrams_empty = self.anagram_generator.generate('')
        self.assertEqual(len(anagrams_empty), 0)  # Expect no anagrams for an empty string

if __name__ == '__main__':
    unittest.main()
