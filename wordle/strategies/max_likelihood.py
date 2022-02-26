"""
max_likelihood.py
"""
from wordle.probability_functions.probability_function import ProbabilityFunction
from .strategy import Strategy


class MaxLikelihoodStrategy(Strategy):
    """
    Strategy that chooses the word with the lowest likelihood
    """

    @staticmethod
    def choose_next_word(prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function chooses the word with the greatest probability
        based on prob_func
        :param prob_func: the probability function to use
        :return: the next word to use
        """
        return max(prob_func.word_bank, key=prob_func.calc_prob)
