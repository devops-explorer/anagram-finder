import argparse
from algorithms.anagramgentrie import TrieAnagramStrategy
from factories.filefactory import FileAnagramFactory
from factories.urlfactory import URLAnagramFactory
from anagramgenerator import AnagramGenerator

def main():
    parser = argparse.ArgumentParser(description='Anagram Generation')
    parser.add_argument('source', choices=['file', 'url'], help='Choose data source (file or URL)')
    parser.add_argument('path', help='Path to file or URL')

    args = parser.parse_args()

    if args.source == 'file':
        # Use file-based strategy
        factory = FileAnagramFactory()
        reader = factory.create_reader(args.path)
    elif args.source == 'url':
        # Use URL-based strategy
        factory = URLAnagramFactory()
        reader = factory.create_reader(args.path)

    corpus = [line.strip() for line in reader.read()]

    strategy = TrieAnagramStrategy(corpus)  
    generator = AnagramGenerator(strategy)

    for line in corpus:
        anagrams = generator.generate(line)
        if anagrams:
            print(f"{line},")
            for anagram in anagrams:
                print(f"{line}, {' '.join(anagram)}")
        print()

if __name__ == "__main__":
    main()