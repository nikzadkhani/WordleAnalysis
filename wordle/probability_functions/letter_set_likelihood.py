"""
letter_set_likelihood.py
"""
from typing import Dict
import numpy as np

from ..constants import VOWELS, CONSONANTS, ALPHABET
from ..words.word_bank import WordBank
from .probability_function import ProbabilityFunction


class LetterSetLikelihood(ProbabilityFunction):
    """Calculates the probability of a word based on the sum of each letter
    occuring in the word. The letters are viewed as a set, such that a word's
    anagrams will yield the same probabilities as the original word and
    to each other.
    """

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

    @staticmethod
    def calc_prob(word_bank: WordBank, word: str) -> float:
        mapping = LetterSetLikelihood.generate_mapping(word_bank)
        return sum(mapping[letter] for letter in word)

    @staticmethod
    def calc_prob_of_consonants(word_bank: WordBank, word: str) -> float:
        mapping = LetterSetLikelihood.generate_mapping(word_bank)
        return sum(mapping[letter] for letter in word if letter in CONSONANTS)

    @staticmethod
    def calc_prob_of_vowels(word_bank: WordBank, word: str) -> float:
        mapping = LetterSetLikelihood.generate_mapping(word_bank)
        return sum(mapping[letter] for letter in word if letter in VOWELS)
