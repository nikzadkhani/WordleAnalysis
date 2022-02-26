#
# letter_likelihood_sum.py

# TODO:
#   - Add remove impossible words, think if this should be added to prob function
#

from ..constants import VOWELS, CONSONANTS, ALPHABET
from probability_function import ProbabilityFunction
from typing import List, Dict

import numpy as np


class LetterSetLikelihood(ProbabilityFunction):
    """Calculates the probability of a word based on the sum of each letter
    occuring in the word. The letters are viewed as a set, such that a word's
    anagrams will yield the same probabilities as the original word and
    to each other.

    :param word_bank: A list of words to be used as the word bank.
    """

    def __init__(self, word_bank: List[str]):
        super().__init__(word_bank)
        self.mapping = self.generate_mapping(word_bank)

    def generate_mapping(self) -> Dict[str, float]:
        """Calculates the probability of a letter appearing in the letter set based
        off the word bank.
        :return: A dictionary mapping each letter to its probability of appearing in
        the set. [0, 1]
        """
        long_str = list("".join(self.word_bank))  # list of letters in bank
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
        return sum(self.mapping[letter] for letter in word)

    def calc_prob_of_consonants(self, word: str) -> float:
        return sum(self.mapping[letter] for letter in word if letter in CONSONANTS)

    def calc_prob_of_vowels(self, word: str) -> float:
        return sum(self.mapping[letter] for letter in word if letter in VOWELS)
