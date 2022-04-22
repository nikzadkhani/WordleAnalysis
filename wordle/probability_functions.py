from abc import abstractmethod, ABC
from typing import List, Dict

from .constants import ALPHABET, CONSONANTS, VOWELS
from .words.word_bank import WordBank

import numpy as np


class ProbabilityFunction(ABC):
    """base class of probability function"""

    def __init__(self, word_bank: WordBank):
        self._word_bank = word_bank

    @abstractmethod
    def calc_prob(self, word: str) -> float:
        """calculate the probability of choosing the word
        according to this function
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    @abstractmethod
    def calc_prob_of_vowels(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the vowels
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    @abstractmethod
    def calc_prob_of_consonants(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the consonants
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    #######
    # Batch Methods
    #######
    def batch_calc_prob(self, words: List[str]) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob(word)
        return probabilities

    def batch_calc_prob_of_vowels(self, words: List[str]) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob_of_vowels. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob_of_vowels(word)
        return probabilities

    def batch_calc_prob_of_consonants(self, words: List[str]) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob_of_consonants. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob_of_consonants(word)
        return probabilities


class LetterSetLikelihood(ProbabilityFunction):
    """Calculates the probability of a word based on the sum of each letter
    occuring in the word. The letters are viewed as a set, such that a word's
    anagrams will yield the same probabilities as the original word and
    to each other.
    """

    def __init__(self, word_bank: WordBank):
        super().__init__(word_bank)
        self._mapping = self.generate_mapping(word_bank)

    def set_word_bank(self, word_bank: WordBank):
        """setter for word bank"""
        self._word_bank = word_bank
        self._mapping = self.generate_mapping(word_bank)

    def get_word_bank(self):
        """getter for word bank"""
        return self._word_bank

    @staticmethod
    def generate_mapping(word_bank) -> Dict[str, float]:
        """Calculates the probability of a letter appearing in the letter set based
        off the word bank.
        :return: A dictionary mapping each letter to its probability of appearing in
        the set. [0, 1]
        """
        long_str = list("".join(word_bank))  # list of letters in bank
        letters, counts = np.unique(long_str, return_counts=True)

        total_letters = sum(counts)
        probabilities = [count / total_letters for count in counts]

        letter_to_prob = dict(zip(letters, probabilities))

        # Add the probability of a letter not appearing in the word bank
        for letter in ALPHABET:
            if letter not in letter_to_prob:
                letter_to_prob[letter] = 0.0

        return letter_to_prob

    def calc_prob(self, word: str) -> float:
        return sum(self._mapping[letter] for letter in word)

    def calc_prob_of_consonants(self, word: str) -> float:
        return sum(self._mapping[letter] for letter in word if letter in CONSONANTS)

    def calc_prob_of_vowels(self, word: str) -> float:
        return sum(self._mapping[letter] for letter in word if letter in VOWELS)


class LetterPositionLikelihood(ProbabilityFunction):
    """Calculates probability of a word based on the likelihood that the letter could
    appear in its given position in the word"""

    def __init__(self, word_bank: WordBank):
        super().__init__(word_bank)
        self._mapping = self.generate_mapping(word_bank)

    def set_word_bank(self, word_bank: WordBank):
        """setter for word bank"""
        self._word_bank = word_bank
        self._mapping = self.generate_mapping(word_bank)

    def get_word_bank(self):
        """getter for word bank"""
        return self._word_bank

    def generate_mapping(self, word_bank: WordBank) -> Dict[int, Dict[str, float]]:
        """
        Generates a mapping of letter position to letter probability. The map
        is first indexed by position, then by letter.
        :return: A mapping of position and letter to its probability.
        """
        count = 0
        pos_to_letter_to_prob = {}
        for word in word_bank:
            count += 1
            for pos, letter in enumerate(word):
                if pos not in pos_to_letter_to_prob:
                    pos_to_letter_to_prob[pos] = {letter: 0}
                if letter not in pos_to_letter_to_prob[pos]:
                    pos_to_letter_to_prob[pos][letter] = 0
                pos_to_letter_to_prob[pos][letter] += 1

        total_num_letters = sum(
            pos_to_letter_to_prob[pos][letter]
            for pos in pos_to_letter_to_prob
            for letter in pos_to_letter_to_prob[pos]
        )

        for pos in pos_to_letter_to_prob:
            # Convert counts to probabilities
            for letter in pos_to_letter_to_prob[pos]:
                pos_to_letter_to_prob[pos][letter] /= total_num_letters

            # Add missing letters
            for letter in ALPHABET:
                if letter not in pos_to_letter_to_prob[pos]:
                    pos_to_letter_to_prob[pos][letter] = 0

        return pos_to_letter_to_prob

    def calc_prob(self, word: str) -> float:
        return sum(self._mapping[pos][letter] for pos, letter in enumerate(word))

    def calc_prob_of_vowels(self, word: str) -> float:
        return sum(
            self._mapping[pos][letter]
            for pos, letter in enumerate(word)
            if letter in VOWELS
        )

    def calc_prob_of_consonants(self, word: str) -> float:
        return sum(
            self._mapping[pos][letter]
            for pos, letter in enumerate(word)
            if letter in CONSONANTS
        )
