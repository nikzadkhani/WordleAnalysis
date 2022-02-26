#
# constants.py
#
# Finish enum and upgrade to 3.10.2

from enum import Enum


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class LetterState(Enum):
    GREY = False
    YELLOW = True
    GREEN = True
