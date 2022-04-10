"""
strategy.py
"""
from abc import ABC, abstractmethod

from ..probability_functions.probability_function import ProbabilityFunction
from ..words.word_bank import WordBank


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
