#
# constants.py
#
# Finish enum and upgrade to 3.10.2

from enum import Enum


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class LetterState(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2
