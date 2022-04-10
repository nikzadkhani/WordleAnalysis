#
# main.py
#
# entrypoint to execute stuff in wordle package
#
from typing import Dict
import pathlib
import logging
import argparse
from unicodedata import name
import wordle
from wordle.helpers import (
    find_available_word_banks,
    find_available_probability_functions,
    find_available_strategies,
)
from wordle.strategies.strategy import Strategy
from wordle.probability_functions.probability_function import ProbabilityFunction
from wordle.wordle import Wordle


def main():
    """
    Main entrypoint for the wordle package.
    """
    parser = argparse.ArgumentParser(description="Run the wordle package code")
    parser.add_argument(
        "action", help="What action to take", choices=["play", "process_bank"]
    )
    parser.add_argument("num_letters", type=int, help="How long the words should be")
    parser.add_argument("num_guesses", type=int, help="How many guesses the user has")

    # Checks functions in strategies module that are not built-ins
    strats: Dict[str, Strategy] = find_available_strategies()
    parser.add_argument(
        "-s",
        "--strategy",
        type=str,
        help="Strategy to use",
        choices=strats,
        default="MaxLikelihoodStrategy",
    )

    prob_fcns: Dict[str, ProbabilityFunction] = find_available_probability_functions()
    parser.add_argument(
        "-p",
        "--probability_function",
        type=str,
        help="Probability function to use",
        choices=prob_fcns,
        default="LetterPositionLikelihood",
    )

    banks: Dict[str, str] = find_available_word_banks()
    parser.add_argument(
        "-w",
        "--word_bank",
        type=str,
        help="File to read the word bank from",
        choices=banks.keys(),
    )

    parser.add_argument(
        "--debug",
        help="Print debug messages",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.action == "play":
        game = Wordle(
            prob_fcns[args.probability_function],
            strats[args.strategy],
            banks[args.word_bank],
            args.num_guesses,
        )
        game.play()


if __name__ == "__main__":
    # main()
    print(find_available_probability_functions())
    # import importlib
    # for module in
    # importlib.import_module()
