# Anagram Generator

This project implements an Anagram Generator using a Trie data structure and various factories for different data sources.

## Components

### Trie

- `Trie` class: Implements a trie data structure for efficient word storage.
- Methods:
  - `add(word)`: Adds a word to the Trie.
  - `__contains__(word)`: Checks if a word is present in the Trie.

### TrieAnagramStrategy

- `TrieAnagramStrategy` class: Generates anagrams using the Trie data structure.
- Methods:
  - `generate(string)`: Generates anagrams for a given string.

### Factories

#### FileAnagramFactory

- `FileAnagramFactory` class: Creates file-based readers and anagram algorithms.

#### URLAnagramFactory

- `URLAnagramFactory` class: Creates URL-based readers and another anagram algorithm.

### Readers

#### FileReader

- `FileReader` class: Reads words from a local file.
- Methods:
  - `read()`: Reads words from a file and returns a list of words.

#### URLReader

- `URLReader` class: Fetches data from a URL.
- Methods:
  - `read()`: Fetches data from a URL and returns a list of strings.

### AnagramGenerator

- `AnagramGenerator` class: Uses a specified strategy to generate anagrams.
- Methods:
  - `generate(corpus)`: Generates anagrams based on the provided corpus using the selected strategy.

## Usage

### Running Anagram Generation

1. Run `main.py` with the following arguments:
   - `source`: Choose data source (`file` or `url`).
   - `path`: Path to the file or URL containing words.
   Example:
   python src/cli.py file .\utils\anagrams.txt
2. Anagrams will be generated for the provided words using the Trie-based strategy.

Examples:
python src/cli.py file .\utils\anagrams.txt  
python src/cli.py url https://raw.githubusercontent.com/dwyl/english-words/master/words.txt

### Running Tests

- Run tests for different components using the provided test files:
- `test_file_reader.py`
- `test_trie.py`
- `test_generator.py`
- `test_performance.py`
- `test_url_reader.py`

Example:
python -m unittest .\tests\test_generator.py

## Testing

- Unit tests cover various functionalities and edge cases for the implemented components.

## Performance

- The `PerformanceTestCase` measures the performance of anagram generation for a given corpus.

## Docker

To build and run the Anagram Generator using Docker, follow these steps:

### Build Docker Image

1. Ensure Docker is installed on your machine.
2. Clone the repository:

   ```bash
   git clone https://github.com/devops-explorer/anagram-finder.git
   cd anagram-finder
   docker build -t my-anagram-app .
   docker run my-anagram-app
   ```

## Workflows

### Available Workflows

#### Docker Build and Run Workflow

This workflow automates the building and running and publishing of the Anagram Generator using Docker. 

#### Publish Package to PyPI Workflow

This workflow builds and publishes the Anagram Generator package to PyPI.

#### Python Tests Workflow

This workflow runs automated tests for different components of the Anagram Generator.

Please refer to the `.github/workflows` directory for detailed YAML files of these workflows.
