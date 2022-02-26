"""
min_likelihood.py
"""
from wordle.probability_functions.probability_function import ProbabilityFunction
from .strategy import Strategy


class MinLikelihoodStrategy(Strategy):
    """
    Strategy that chooses the word with the lowest likelihood
    """

    @staticmethod
    def choose_next_word(prob_func: ProbabilityFunction) -> str:
        """
        Given a probability function chooses the word with the least probability
        based on prob_func
        :param prob_func: the probability function to use
        :return: the next word to use
        """
        return min(prob_func.word_bank, key=prob_func.calc_prob)
