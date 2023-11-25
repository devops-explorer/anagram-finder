import unittest
from src.readers.filereader import FileReader

class TestFileReader(unittest.TestCase):

    def test_read_file_exists(self):
        file_path = 'utils/anagrams.txt'  # Replace with an existing file path for testing
        reader = FileReader(file_path)
        data = reader.read()
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)
        # Add more assertions based on what's expected from the file content

    def test_read_file_not_exists(self):
        file_path = 'nonexistent_file.txt'  # Replace with a non-existent file path for testing
        reader = FileReader(file_path)
        with self.assertRaises(FileNotFoundError):
            reader.read()

if __name__ == '__main__':
    unittest.main()
