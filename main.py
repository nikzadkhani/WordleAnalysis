#
# main.py
#
# entrypoint to execute stuff in wordle package
#

from typing import Dict
import logging
import argparse

from wordle.helpers import find_available_word_banks

import wordle.strategies as strats
import wordle.probability_functions as p_fcns

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

    parser.add_argument(
        "-s",
        "--strategy",
        type=str,
        help="Strategy to use",
        default="MaxLikelihoodStrategy",
    )

    parser.add_argument(
        "-p",
        "--probability_function",
        type=str,
        help="Probability function to use",
        default="LetterPositionLikelihood",
    )

    banks: Dict[str, str] = find_available_word_banks()
    parser.add_argument(
        "-w",
        "--word_bank",
        type=str,
        help="File to read the word bank from",
        choices=banks.keys(),
        default="wordle/wordle_bank",
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

    available_strategies = [
        strat for strat in dir(strats) if not strat.startswith("__")
    ]
    if args.strategy not in available_strategies:
        raise ImportError(
            f"{args.strategy} is not an available strategy.\n"
            "Please check stratgies.py for available stragies.\n"
        )
    strat = getattr(strats, args.strategy)

    available_prob_fcns = [fcn for fcn in dir(p_fcns) if not fcn.startswith("__")]
    if args.probability_function not in available_prob_fcns:
        raise ImportError(
            f"{args.probability_function} is not an available strategy.\n"
            "Please check stratgies.py for available stragies.\n"
        )
    p_fcn = getattr(p_fcns, args.probability_function)

    if args.action == "play":
        game = Wordle(
            p_fcn,
            strat,
            banks[args.word_bank],
            args.num_guesses,
        )
        game.play()


if __name__ == "__main__":
    main()
