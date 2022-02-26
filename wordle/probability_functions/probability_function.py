#
# probability_function.py
#
# Base class for a probability function used in wordle game for evaluating
# the likelihood of choosing a word as the guess. Expecting the __init__
# method to be overwritten to take in a dict mapping of some sort and
# calculate probabilities based off of that mapping. No mapping is defined
# to leave it up to the imagination.
#


from abc import abstractmethod, ABC
from typing import List


class ProbabilityFunction(ABC):
    """base class of probability function"""

    def __init__(self, word_bank: List[str]):
        self.word_bank = word_bank

    ###
    # BASE METHODS
    ###
    @abstractmethod
    def calc_prob(self, word: str) -> float:
        """calculate the probability of choosing the word
        according to this function
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """
        pass

    @abstractmethod
    def calc_prob_of_vowels(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the vowels
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """
        pass

    @abstractmethod
    def calc_prob_of_consonants(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the consonants
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """
        pass

    ###
    # BATCH METHODS
    ###
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
