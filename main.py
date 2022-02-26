#
# main.py
#
# entrypoint to execute stuff in wordle package
#

import logging
import argparse
from wordle.wordle import Wordle


def main():
    """
    Main entrypoint for the wordle package.
    """
    parser = argparse.ArgumentParser(description="Run the wordle package code")
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

    # wordle = Wordle()
    # wordle.play()


if __name__ == "__main__":
    main()
