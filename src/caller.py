from algorithms.anagramgentrie import AnagramGenerator


with open('utils/anagrams.txt', 'r') as file:
    corpus = [line.strip() for line in file.readlines()]

gen = AnagramGenerator(corpus)

for line in corpus:
    anagrams = gen.generate(line)
    if anagrams:
        print(f"{line},")
        for anagram in anagrams:
            print(f"{line}, {' '.join(anagram)}")
        print()
