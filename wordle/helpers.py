#
# helpers.py
#

from colorama import Fore
from typing import Dict
import pathlib

from .constants import LetterState


def find_available_word_banks() -> Dict[str, str]:
    """
    Finds all available word banks in the word_banks module
    """
    words_dir = pathlib.Path(__file__).parent.joinpath("words")
    available_word_banks = {}
    for folder in words_dir.iterdir():
        if folder.is_dir() and not folder.name.startswith("__"):
            for file in folder.glob("*.txt"):
                available_word_banks[f"{folder.name}/{file.name.rstrip('.txt')}"] = file

    return available_word_banks


def state_to_color(letter_state: LetterState):
    """Converts letter state to its respective color"""
    match letter_state:
        case LetterState.GREEN:
            return Fore.GREEN
        case LetterState.YELLOW:
            return Fore.YELLOW
        case _:
            return Fore.WHITE
