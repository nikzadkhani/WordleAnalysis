"""
probability_function.py

Base class for a probability function used in wordle game for evaluating
the likelihood of choosing a word as the guess. Keeps state on the word bank with
functionality to shorten the bank depending on guesses.
"""


from abc import abstractmethod, ABC
from typing import List

from ..words.word_bank import WordBank


class ProbabilityFunction(ABC):
    """base class of probability function"""

    @staticmethod
    @abstractmethod
    def calc_prob(word_bank: WordBank, word: str) -> float:
        """calculate the probability of choosing the word
        according to this function
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    @staticmethod
    @abstractmethod
    def calc_prob_of_vowels(word_bank: WordBank, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the vowels
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    @staticmethod
    @abstractmethod
    def calc_prob_of_consonants(word_bank: WordBank, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the consonants
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    #######
    # Batch Methods
    #######
    def batch_calc_prob(self, word_bank: WordBank, words: List[str]) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob(word_bank, word)
        return probabilities

    def batch_calc_prob_of_vowels(
        self, word_bank: WordBank, words: List[str]
    ) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob_of_vowels. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob_of_vowels(word_bank, word)
        return probabilities

    def batch_calc_prob_of_consonants(
        self, word_bank: WordBank, words: List[str]
    ) -> List[float]:
        """Given a list of words, calculate the probability of choosing
        each word according to calc_prob_of_consonants. The probabilities are calculated
        independently for each word.
        :param words: the list of words we should calculate the probability
        :return: the list of probabilities we choose each word
        """
        probabilities = [0.0] * len(words)
        for i, word in enumerate(words):
            probabilities[i] = self.calc_prob_of_consonants(word_bank, word)
        return probabilities
