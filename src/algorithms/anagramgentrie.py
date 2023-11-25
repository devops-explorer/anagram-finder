from .ianagramstrategy import AnagramStrategy

class Trie:
    """
    A Trie data structure for storing words efficiently.
    """

    def __init__(self):
        """
        Initializes the Trie with an empty root node.
        """
        self.root = {}

    def add(self, word):
        """
        Adds a word to the Trie.

        Args:
        - word (str): The word to be added.
        """
        if len(word) > 0:
            self.__add(self.root, word[0], word[1:])

    def __add(self, node, prefix, suffix):
        """
        Recursive function to add a word to the Trie.

        Args:
        - node (dict): Current node in the Trie.
        - prefix (str): Current character to add to the Trie.
        - suffix (str): Remaining characters of the word to add.
        """
        if prefix not in node:
            node[prefix] = {}
        if suffix == "":
            node[prefix][suffix] = ""
        else:
            new_prefix = suffix[0]
            new_suffix = suffix[1:]
            self.__add(node[prefix], new_prefix, new_suffix)

    def __contains__(self, word):
        """
        Checks if a word is present in the Trie.

        Args:
        - word (str): The word to search for in the Trie.

        Returns:
        - bool: True if the word is present, False otherwise.
        """
        word = list(word)
        index_string = "['" + "']['".join(word) + "']"
        try:
            child_nodes = eval("self.root"+index_string)
            if '' in child_nodes:
                return True
        except KeyError:
            pass
        return False


class TrieAnagramStrategy(AnagramStrategy):
    """
    Generates anagrams based on a given corpus using Trie data structure.
    """

    def __init__(self, corpus):
        """
        Initializes the AnagramGenerator with a Trie built from the provided corpus.

        Args:
        - corpus (list): List of words to build the Trie.
        """
        self.t = Trie()
        for word in corpus:
            word = word.rstrip()
            self.t.add(word)

    def frequency_dict(self, string):
        """
        Generates a frequency dictionary for characters in a string.

        Args:
        - string (str): Input string.

        Returns:
        - dict: Frequency dictionary for characters in the string.
        """
        f = {}
        for letter in string:
            if letter not in f:
                f[letter] = 0
            f[letter] += 1
        return f

    def generate(self, string):
        """
        Generates anagrams for a given string.

        Args:
        - string (str): Input string to generate anagrams.

        Returns:
        - list: List of generated anagrams.
        """
        string = string.lower()
        for c in string:
            if c not in 'abcdefghijklmnopqrstuvwxyz':
                string = string.replace(c, "")

        anagrams = []
        f = self.frequency_dict(string)
        self.__generate(anagrams, self.t.root, [], "", f)

        return anagrams

    def __generate(self, anagrams, node, partial_anagram, current_word, f):
        """
        Recursive function to generate anagrams.

        Args:
        - anagrams (list): List to store generated anagrams.
        - node (dict): Current node in the Trie.
        - partial_anagram (list): Partially generated anagram.
        - current_word (str): Current word in the anagram.
        - f (dict): Frequency dictionary for characters.
        """
        if '' in node: # if we have just finished generating a word
            next_partial_anagram = partial_anagram + [current_word]
            if all([f[key] == 0 for key in f]): # if there are no more letters
                anagrams.append(next_partial_anagram) # then this is a full phrase anagram
            else:
                self.__generate(anagrams, self.t.root, next_partial_anagram, "", f) # so loop back to the top of the tree with a new word and add a space to the anagram phrase we are building

        for prefix in f:
            if f[prefix] > 0:
                if prefix in node:
                    new_word = current_word+prefix
                    if len(partial_anagram) == 0 or new_word >= partial_anagram[-1][:len(new_word)]:
                        f[prefix] -= 1 # since f is shared between function calls we need to subtract from it
                        self.__generate(anagrams, node[prefix], partial_anagram, current_word+prefix, f)
                        f[prefix] += 1 # then add back
