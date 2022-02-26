#
# process_banks.py
#
# Used to generate new word banks for different wordle strategies/games
#
# TODO:
#  - Add Cmd line arguments
#

import os
from typing import List
import numpy as np

# Path to the directory this file is in
PACKAGE_DIR = os.path.dirname(__file__)

# Wordle bank directories
WIKIPEDIA_DIR = os.path.join(PACKAGE_DIR, "words/wikipedia/")
WORDLE_BANK_DIR = os.path.join(PACKAGE_DIR, "words/wordle")

# WIKIPEDIA FILES
WIKIPEDIA_WORD_FILE = os.path.join(WIKIPEDIA_DIR, "words_alpha.txt")
SUBSET_FILE_TEMPLATE = os.path.join(WIKIPEDIA_DIR, "{}_letter_words.txt")

# WORDLE BANK FILES


VOWELS = "aeiouy"


def generate_wikipedia_words_subset(num_letters: int, words_file: str) -> None:
    """ Generate a new file that only has words found in words_file of length
    num_letters.
    :param num_letters: number of letters words should have in new file
    :param words_file: path to the a text file containing the words to sift
    through, it is expected that the words in words_file will be newline 
    seperated
    """
    with open(SUBSET_FILE_TEMPLATE.format(num_letters), 'w+') as f:
        for word in open(words_file, 'r'):
            word = word.replace('\n', '')  # Remove new lines
            if len(word) == num_letters:
                f.write(f"{word}\n")


def generate_words_with_unique_letters(words_file) -> None:
    """ Writes a new files that contains only the words with all unique letters
    from the source file. ie. table would be included, but abbey will not since
    the b does not have a unique position. In other words this removes words
    with double letters and up (triple, quadruple?, etc.).

    The file generated will be generated in the same directory as words_file,
    and it will be called the same thing with 'unique' prefixed to the file
    name.

    :param words_file: path to the file with new line seperated words
    """
    file_name = os.path.basename(words_file)
    file_dir = os.path.dirname(words_file)
    unique_file_name = os.path.join(file_dir, f"unique_{file_name}")

    with open(words_file, 'r') as f:
        with open(unique_file_name, 'w+') as unique_f:
            for word in f:
                word = word.replace("\n", "")
                if len(np.unique(list(word))) == len(word):
                    unique_f.write(word + "\n")


def load_words(word_file) -> List[str]:
    """ Reads words from a word file and returns of the list of the words
    in the file.
    :param word_file: path to a newline seperated file with words.
    """
    word_array = []
    with open(word_file, 'r') as f:
        for word in f:
            word = word.replace('\n', '')
            word_array.append(word)
    return word_array


def main():
    pass


if __name__ == '__main__':
    main()
