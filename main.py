#
# Wordle Analysis
#
#

import random
from enum import Enum, auto
from numpy import unique
from typing import Dict, List

WORD_FILE = "words_alpha.txt"
WORD_FILE_TEMPLATE = "{}_letter_words.txt"
VOWELS = "aeiouy"
MAX_TRIES = 6


def sift_words(num_letters, words_file):
    with open(WORD_FILE_TEMPLATE.format(num_letters), 'w+') as f:
        for word in open(words_file, 'r'):
            word = word.replace("\n", "")  # Remove new lines
            if len(word) == num_letters:
                f.write(word + "\n")


def sift_repetitions(words_file):
    with open(words_file, 'r') as f:
        with open(f"unique_{words_file}", 'w+') as unique_f:
            for word in f:
                word = word.replace("\n", "")
                if len(unique(list(word))) == len(word):
                    unique_f.write(word + "\n")


def load_words(word_file) -> List[str]:
    word_array = []
    with open(word_file, 'r') as f:
        for word in f:
            word = word.replace('\n', '')
            word_array.append(word)
    return word_array


class Wordle:
    def __init__(self, word_bank, strategy="ML", use_per_pos_probs=True, max_tries=6):
        self.original_bank = word_bank
        self.max_tries = max_tries
        self.word_bank = word_bank
        self.game_finished = False
        self.word_goal = self.generate_random_word(word_bank)
        self.strategy = strategy.upper()
        self.use_per_pos_probs = use_per_pos_probs
        assert(strategy == "ML" or strategy == "LL" or strategy == "ALT", "BASTARD, yaint a strategy")

    def generate_random_word(word_array):
        random_word = word_array[random.randint(0, len(word_array))]
        return random_word

    def calc_letter_prob(word_array) -> Dict[str, int]:
        letter_probabilities = {}
        total_letters = 0
        for word in word_array:
            for letter in word:
                total_letters += 1
                if letter in letter_probabilities:
                    letter_probabilities[letter] += 1
                else:
                    letter_probabilities[letter] = 1

        for letter, num_occurrences in letter_probabilities.items():
            letter_probabilities[letter] = num_occurrences/total_letters

        return letter_probabilities

    def calc_letter_prob_per_pos(word_array) -> Dict[int,
                                                     Dict[str, int]]:
        letter_probabilities = {}
        total_letters = 0
        for word in word_array:
            for position in range(len(word)):
                total_letters += 1
                if position in letter_probabilities:
                    if word[position] in letter_probabilities[position]:
                        letter_probabilities[position][word[position]] += 1
                    else:
                        letter_probabilities[position][word[position]] = 1
                else:
                    letter_probabilities[position] = {}
                    letter_probabilities[position][word[position]] = 1

        for position, letter_dict in letter_probabilities.items():
            for letter, num_occurrences in letter_dict.items():
                letter_probabilities[position][letter] = num_occurrences/total_letters

        return letter_probabilities

    def calc_word_prob(word, letter_probabilities: Dict[str, int]) -> float:
        probability = 0
        for letter in word:
            probability += letter_probabilities[letter]
        return probability

    def calc_word_prob_with_pos(
            word, letter_probabilities_by_position: Dict
            [int, Dict[str, int]]) -> float:
        probability = 0
        for i, letter in enumerate(word):
            probability += letter_probabilities_by_position[i][letter]
        return probability

    def calc_word_prob_consonant(
            word, letter_probabilities: Dict[str, int]) -> float:
        probability = 0
        for letter in word:
            if letter not in VOWELS:
                probability += letter_probabilities[letter]
        return probability

    def calc_word_prob_consonant_with_pos(word,
                                          letter_probabilities_by_position:
                                          Dict[int, Dict[str, int]]) -> float:
        probability = 0
        for i, letter in enumerate(word):
            if letter not in VOWELS:
                probability += letter_probabilities_by_position[i][letter]
        return probability

    def find_most_likely_word(
            probability_fcn, probability_dict, word_array) -> str:
        # TODO: interface the parameters or curry whichever is more big brain
        highest_prob = 0
        most_likely_word = ""
        for word in word_array:
            if (probability := probability_fcn(word, probability_dict)) > highest_prob:
                most_likely_word = word
                highest_prob = probability
        return most_likely_word

    def find_least_likely_word(
            probability_fcn, probability_dict, word_array) -> str:
        # TODO: interface the parameters or curry whichever is more big brain
        lowest_prob = 0
        least_likely_word = ""
        for word in word_array:
            if (probability := probability_fcn(word, probability_dict)) < lowest_prob:
                least_likely_word = word
                lowest_prob = probability
        return least_likely_word

    def play(self):
        #TODO: be epic with 3.10
        guesses = 0
        while not self.game_finished and guesses < self.max_tries:
            letter_prob = self.calc_letter_prob(self.word_bank)
            letter_prob_by_pos = self.calc_letter_prob_per_pos(self.word_bank)

            

            if self.strategy == "ML":
                pass
            elif self.strategy == "LL":
                pass
            elif self.strategy == "ALT":
                pass
            else:
                raise ValueError("How you did this maaan??")
                                
            guesses += 1
            
def main():
    file = WORD_FILE_TEMPLATE.format('5')
    sift_words(5, WORD_FILE)
    sift_repetitions(file)
    word_array = load_words(f"unique_{file}")
    letter_prob = calc_letter_prob(word_array)
    letter_prob_by_pos = calc_letter_prob_per_pos(
        word_array)

    print(find_most_likely_word(
        calc_word_prob, letter_prob, word_array))
    print(
        find_most_likely_word(
            calc_word_prob_with_pos,
            letter_prob_by_pos, word_array))
    print(find_most_likely_word(
        calc_word_prob_consonant, letter_prob, word_array))
    print(find_most_likely_word(
        calc_word_prob_consonant_with_pos,
        letter_prob_by_pos, word_array))


if __name__ == '__main__':
    main()
