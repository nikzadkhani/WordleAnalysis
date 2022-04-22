"""
word_bank.py
"""
from typing import List, Tuple

from wordle.constants import ALPHABET, LetterState


class WordBank:
    """
    WordBank that contains a list of words. Treat as a list with some extra goodies
    like filtering and loading from file.
    """

    def __init__(self, file_path):
        self.original_word_bank = self.load_words(file_path)
        self.word_bank = self.original_word_bank.copy()

    def reset_bank(self) -> None:
        """Resets the word bank to the original word bank."""
        self.word_bank = self.original_word_bank.copy()

    def load_words(self, file_path) -> List[str]:
        """Reads words from a word file and returns of the list of the words
        in the file.
        :param word_file: path to a newline seperated file with words.
        """
        word_array = []
        with open(file_path, "r", encoding="utf-8") as f:
            for word in f:
                word = word.replace("\n", "")
                word_array.append(word)
        return word_array

    def filter_bank(self, guess: List[Tuple[str, LetterState]]) -> None:
        """Given a guess to the word, remove words that cannot be the real answer
        based off the guess's letter states.
        :param guess: the guess to the word represented as a list of (letter, state)
        """
        self.word_bank = [
            word for word in self.word_bank if self.is_possible_word(word, guess)
        ]

    @staticmethod
    def is_possible_word(_word: str, guess: List[Tuple[str, LetterState]]) -> None:
        """Given a guess state check if the given word could be the goal word"""
        word = list(_word)
        for i, (guess_letter, state) in enumerate(guess):
            if state == LetterState.GREEN:
                if word[i] != guess_letter:

                    return False
                word[i] = ""
        for i, (guess_letter, state) in enumerate(guess):
            if state == LetterState.YELLOW:
                if guess_letter not in word or guess_letter == word[i]:
                    return False
                # consume the yellow letter
                word[word.index(guess_letter)] = ""
        for i, (guess_letter, state) in enumerate(guess):
            if state == LetterState.GREY and (guess_letter in word):
                return False

        return True

    def filtered_bank(self, guess: List[Tuple[str, LetterState]]) -> None:
        """Given a guess to the word, calculate what the next word bank should be
        :param guess: the guess to the word represented as a list of (letter, state)
        """
        for word in self.word_bank:
            for i, (guess_letter, state) in enumerate(guess):
                match state:
                    case LetterState.GREY:
                        if guess_letter in word:
                            self.word_bank.remove(word)
                            break
                    case LetterState.YELLOW:
                        if word[i] == guess_letter or guess_letter not in word:
                            self.word_bank.remove(word)
                            break
                    case LetterState.GREEN:
                        if word[i] != guess_letter:
                            self.word_bank.remove(word)
                            break
                    case _:
                        raise ValueError(f"unknown letter state: {state}")

    def bank_letter_matrix(self) -> List[List[int]]:
        """
        :return: a matrix of the letters in the word bank
        """
        # Initialize 26 by len(words in bank) matrix
        matrix = [[0] * len(self.word_bank[0]) for _ in range(len(ALPHABET))]
        for word in self.word_bank:
            for i, letter in enumerate(word):
                matrix[ALPHABET.index(letter)][i] += 1
        return matrix

    def remove(self, word):
        """Removes the word from the word bank"""
        self.word_bank.remove(word)

    def print_bank(self):
        for i, word in enumerate(self.word_bank):
            print(word, end=" ")
            if i % 15 == 0:
                print()

    @staticmethod
    def print_list(ls):
        for i, word in enumerate(ls):
            print(word, end=" ")
            if i % 15 == 0:
                print()

    def __str__(self):
        return self.__class__.__name__

    def __getitem__(self, item):
        return self.word_bank[item]

    def __len__(self):
        return len(self.word_bank)
