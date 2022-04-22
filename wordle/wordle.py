#
# wordle.py
#
# wordle game class for running analysis/game
#


import logging
import random
from typing import List, Tuple
from colorama import init, Fore


from wordle.constants import LetterState
from wordle.probability_functions import ProbabilityFunction
from wordle.strategies import Strategy
from wordle.words.word_bank import WordBank
from wordle.helpers import state_to_color

init()


class Wordle:
    """main game loop"""

    def __init__(
        self,
        prob_func: ProbabilityFunction,
        strategy: Strategy,
        word_bank_file_path: str,
        max_tries: int,
        filter_bank=True,
    ):
        self.prob_func = prob_func
        self.strategy = strategy
        self.word_bank = WordBank(word_bank_file_path)
        self.max_tries = max_tries
        self.filter_bank = filter_bank

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
        self.guesses = []
        self.guess_states = []

        self.goal_word = random.choice(self.word_bank)
        logging.debug("Goal word: %s", self.goal_word)

        self.tries = 0

    def get_guess_state(self, guess: str) -> List[Tuple[str, LetterState]]:
        """Given a letter guess, return the Wordle colors of each letter after the
        guess was submitted. In other words the colors of the tiles after they flipped.
        :param: guess a str containing the guess
        :return: a list of tuples containing the letter and its color state.

        for example this might return
        [("f", LetterState.Green), ("o", LetterState.Yellow), ("o", LetterState.Grey)]
        """
        _goal_word = list(self.goal_word)
        guess_state = [0] * len(self.goal_word)
        for i, letter in enumerate(guess):
            if letter == _goal_word[i]:
                guess_state[i] = (letter, LetterState.GREEN)
                _goal_word[i] = ""

        for i, letter in enumerate(guess):
            if letter in _goal_word:
                guess_state[i] = (letter, LetterState.YELLOW)
                _goal_word[i] = ""

        for i, letter in enumerate(guess):
            if guess_state[i] == 0:
                guess_state[i] = (letter, LetterState.GREY)

        return guess_state

    def print_state(self):
        """prints all the guesses in their guess state format"""
        for guess_state in self.guess_states:
            for letter, state in guess_state:
                print(state_to_color(state) + letter, end="")
            print(Fore.WHITE)

    def player_guess(self):
        """get guess from input"""
        guess = input("Guess: ")
        return self.get_guess_state(guess)

    def play(self):
        """Run the game loop"""
        logging.info("Starting Game")

        self.guesses = []
        while not self.game_finished:
            self.tries += 1
            if self.tries > self.max_tries:
                logging.info(
                    "Game over, failed to get goal word: %s", self.goal_word.upper()
                )
                logging.info("Guesses: %s", self.guesses)
                self.game_finished = True
            else:
                guess = self.strategy.choose_next_word(self.word_bank, self.prob_func)
                self.guesses.append(guess.upper())

                logging.info("Guess %d: %s", self.tries, guess)

                guess_state = self.get_guess_state(guess)
                self.guess_states.append(guess_state)

                # Print the guesses wordle style
                self.print_state()

                if self.filter_bank:
                    self.word_bank.filter_bank(guess_state)
                else:
                    self.word_bank.remove(guess)

            if guess == self.goal_word:
                logging.info("Got the goal word after %d tries", self.tries)
                self.game_finished = True
