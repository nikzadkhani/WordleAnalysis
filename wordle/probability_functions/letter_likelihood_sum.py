#
# letter_likelihood_sum.py
#
#

from probability_function import ProbabilityFunction
from typing import List, Dict

import numpy as np


class LetterLikelihoodSum(ProbabilityFunction):
    def __init__(self, word_bank: List[str]):
        super().__init__(word_bank)
        self.mapping = self.generate_mapping(word_bank)

    @staticmethod
    def generate_mapping(word_bank) -> Dict[str, float]:
        """ Given a word bank this function will generate a dictionary/map
        from a single letter to its probability of occuring.
        """
        long_str = list("".join(word_bank))  # list of letters in bank
        letters, counts = np.unique(long_str, return_counts=True)

        total_letters = sum(counts)
        probabilities = [count/total_letters for count in counts]

        return dict(zip(letters, probabilities))

    def calc_prob():

    def calc_prob_of_consonants(self, word: str) -> float:
        pass

    def calc_prob_of_vowels(self, word: str) -> float:
        pass


LetterLikelihoodSum(['hello', 'bye', 'gg'])
