"""
probability_function.py

Base class for a probability function used in wordle game for evaluating
the likelihood of choosing a word as the guess. Keeps state on the word bank with
functionality to shorten the bank depending on guesses.
"""


from abc import abstractmethod, ABC
from typing import List, Tuple

from ..constants import ALPHABET, LetterState


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

    @abstractmethod
    def calc_prob_of_vowels(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the vowels
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

    @abstractmethod
    def calc_prob_of_consonants(self, word: str) -> float:
        """calculate the probability of choosing the word only counting
        the consonants
        :param word: the word we should calculate the probability of
        :return: the probability we choose this word
        """

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

    def filter_bank(self, guess: List[Tuple[str, LetterState]]) -> None:
        """Given a guess to the word, remove words that cannot be the real answer
        based off the guess's letter states.
        :param guess: the guess to the word represented as a list of (letter, state)
        """
        for word in self.word_bank:
            for i, (guess_letter, state) in enumerate(guess):
                match state:
                    case LetterState.GREY:
                        if guess_letter in word:
                            self.word_bank.remove(word)
                            break
                    case LetterState.YELLOW:
                        if word[i] == guess_letter or guess_letter not in word:
                            self.word_bank.remove(word)
                            break
                    case LetterState.GREEN:
                        if word[i] != guess_letter:
                            self.word_bank.remove(word)
                            break
                    case _:
                        raise ValueError(f"unknown letter state: {state}")

    def bank_letter_matrix(self) -> List[List[int]]:
        """
        :return: a matrix of the letters in the word bank
        """
        # Initialize 26 by len(words in bank) matrix
        matrix = [[0] * len(self.word_bank[0]) for _ in range(len(ALPHABET))]
        for word in self.word_bank:
            for i, letter in enumerate(word):
                matrix[ALPHABET.index(letter)][i] += 1
        return matrix

    def __str__(self):
        return self.__class__.__name__
