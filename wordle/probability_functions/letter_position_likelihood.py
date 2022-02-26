#
# letter_position_likelihood.py
#
# TODO:
#   - Finish remove impossible words

from ..constants import VOWELS, CONSONANTS, ALPHABET, LetterState
from typing import Dict, List, Tuple
from probability_function import ProbabilityFunction


class LetterPositionLikelihood(ProbabilityFunction):
    def __init__(self, word_bank: List[str]):
        super().__init__(word_bank)
        self.mapping = self.generate_mapping()

    def generate_mapping(self) -> Dict[int, Dict[str, float]]:
        """
        Generates a mapping of letter position to letter probability. The map
        is first indexed by position, then by letter.
        :return: A mapping of position and letter to its probability.
        """
        pos_to_letter_to_prob = {}
        for word in self.word_bank:
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
        return sum(self.mapping[pos][letter] for pos, letter in enumerate(word))

    def calc_prob_of_vowels(self, word: str) -> float:
        return sum(
            self.mapping[pos][letter]
            for pos, letter in enumerate(word)
            if letter in VOWELS
        )

    def calc_prob_of_consonants(self, word: str) -> float:
        return sum(
            self.mapping[pos][letter]
            for pos, letter in enumerate(word)
            if letter in CONSONANTS
        )

    def remove_impossible_words(self, incorrect_letters: List[Tuple[str, LetterState]]) -> None:
        """Given a list of incorrect letters, remove all words that contain those letters."""
        for word in self.word_bank:
            for 