"""
strategies.py
"""
from abc import ABC, abstractmethod
from random import choice, randint
from .probability_functions import ProbabilityFunction
from .words.word_bank import WordBank


class Strategy(ABC):
    """base class of strategy"""

    @staticmethod
    @abstractmethod
    def choose_next_word(word_bank: WordBank, prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function choose the next word to use
        :param prob_func: the probability function to use
        :return: the next word to use
        """

    def __str__(self):
        return self.__class__.__name__


class RandomAlternating(Strategy):
    """
    Strategy that chooses the word with randomly
    """

    @staticmethod
    def choose_next_word(word_bank: WordBank, prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function and a word bank abides by MaxLikelihoodStrategy
        half the time, and a random word the other half
        :param word_bank: the word bank to choose from
        :param prob_func: the probability function to use
        :return: the next word to use
        """
        return (
            MaxLikelihoodStrategy.choose_next_word(word_bank, prob_func)
            if randint(0, 1)
            else choice(word_bank)
        )


class MinLikelihoodStrategy(Strategy):
    """
    Strategy that chooses the word with the lowest likelihood
    """

    @staticmethod
    def choose_next_word(word_bank: WordBank, prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function chooses a word in word_bank with the
        least probability based on prob_func
        :param word_bank: the word bank to choose from
        :param prob_func: the probability function to use
        :return: the next word to use
        """
        fcn = prob_func(word_bank)
        return min(word_bank, key=fcn.calc_prob)


class MaxLikelihoodStrategy(Strategy):
    """
    Strategy that chooses the word with the lowest likelihood
    """

    @staticmethod
    def choose_next_word(word_bank: WordBank, prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function chooses the word with the greatest probability
        based on prob_func
        :param prob_func: the probability function to use
        :return: the next word to use
        """
        fcn = prob_func(word_bank)
        return max(word_bank, key=fcn.calc_prob)
