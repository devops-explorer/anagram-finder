import unittest
import time
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the directory of the current script and add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.algorithms.anagramgentrie import TrieAnagramStrategy

class PerformanceTestCase(unittest.TestCase):
    def test_performance(self):
        corpus_file = 'utils/anagrams.txt'
        with open(corpus_file, 'r') as file:
            corpus = [line.strip() for line in file.readlines()]

        logging.info("Anagram generation started...")
        start_time = time.time()
        anagram_generator = TrieAnagramStrategy(corpus)
        for word in corpus:
            anagrams = anagram_generator.generate(word)
            formatted_anagrams = ', '.join([''.join(a) for a in anagrams])
            logging.info(f"{word}, {formatted_anagrams}")
        end_time = time.time()

        logging.info(f"All anagrams generated in {end_time - start_time:.4f} seconds.")

if __name__ == '__main__':
    unittest.main()
