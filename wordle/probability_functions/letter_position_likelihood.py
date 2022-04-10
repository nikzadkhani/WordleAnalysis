"""
letter_position_likelihood.py
"""

from typing import Dict

from ..constants import ALPHABET, CONSONANTS, VOWELS
from ..words.word_bank import WordBank
from .probability_function import ProbabilityFunction


class LetterPositionLikelihood(ProbabilityFunction):
    """Calculates probability of a word based on the likelihood that the letter could
    appear in its given position in the word"""

    @staticmethod
    def generate_mapping(word_bank: WordBank) -> Dict[int, Dict[str, float]]:
        """
        Generates a mapping of letter position to letter probability. The map
        is first indexed by position, then by letter.
        :return: A mapping of position and letter to its probability.
        """
        pos_to_letter_to_prob = {}
        for word in word_bank:
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

    @staticmethod
    def calc_prob(word_bank: WordBank, word: str) -> float:
        mapping = LetterPositionLikelihood.generate_mapping(word_bank)
        return sum(mapping[pos][letter] for pos, letter in enumerate(word))

    @staticmethod
    def calc_prob_of_vowels(word_bank: WordBank, word: str) -> float:
        mapping = LetterPositionLikelihood.generate_mapping(word_bank)
        return sum(
            mapping[pos][letter] for pos, letter in enumerate(word) if letter in VOWELS
        )

    @staticmethod
    def calc_prob_of_consonants(word_bank: WordBank, word: str) -> float:
        mapping = LetterPositionLikelihood.generate_mapping(word_bank)
        return sum(
            mapping[pos][letter]
            for pos, letter in enumerate(word)
            if letter in CONSONANTS
        )
