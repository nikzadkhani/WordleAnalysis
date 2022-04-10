#
# wordle.py
#
# wordle game class for running analysis/game
#
# TODO:
#  - Takeout the probability functions and write them to their own files that
#    inherit from the abstract class
#  - write the wordle game

import random
import logging


from wordle.probability_functions.probability_function import ProbabilityFunction
from wordle.strategies.strategy import Strategy
from wordle.words.word_bank import WordBank


class Wordle:
    """main game loop"""

    def __init__(
        self,
        prob_func: ProbabilityFunction,
        strategy: Strategy,
        word_bank_file_path: str,
        max_tries: int,
    ):
        self.prob_func = prob_func
        self.strategy = strategy
        self.word_bank = WordBank(word_bank_file_path)
        self.max_tries = max_tries

        logging.debug(
            "Wordle initialized with \n"
            "Probability Function: %s\n"
            "Strategy: %s\n"
            "Max tries: %d",
            prob_func,
            strategy,
            max_tries,
        )

        self.game_finished = False

        self.goal_word = random.choice(self.word_bank)
        logging.debug("Goal word: %s", self.goal_word)

        self.tries = 0

    def play(self):
        """Run the game loop"""
        guesses = []
        while not self.game_finished:
            self.tries += 1
            if self.tries > self.max_tries:
                logging.info(
                    "Game over, failed to get goal word: %s", self.goal_word.upper()
                )
                logging.info("Guesses: %s", guesses)
                break

            guess = self.strategy.choose_next_word(self.prob_func)
            guesses.append(guess.upper())
            logging.info("Guess %d: %s", self.tries, guess)

            if guess == self.goal_word:
                logging.info("Got the goal word after %d tries", self.tries)
                self.game_finished = True
