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

from typing import Dict, List


class Wordle:
    def __init__(self, word_bank, strategy="ML", use_per_pos_probs=True, max_tries=6):
        self.original_bank = word_bank
        self.max_tries = max_tries
        self.word_bank = word_bank
        self.game_finished = False
        self.word_goal = self.generate_random_word(word_bank)
        self.strategy = strategy.upper()
        self.use_per_pos_probs = use_per_pos_probs
        assert (
            strategy == "ML" or strategy == "LL" or strategy == "ALT",
            "BASTARD, yaint a strategy",
        )

    def generate_random_word(word_array):
        random_word = word_array[random.randint(0, len(word_array))]
        return random_word

    def find_most_likely_word(probability_fcn, probability_dict, word_array) -> str:
        # TODO: interface the parameters or curry whichever is more big brain
        highest_prob = 0
        most_likely_word = ""
        for word in word_array:
            if (probability := probability_fcn(word, probability_dict)) > highest_prob:
                most_likely_word = word
                highest_prob = probability
        return most_likely_word

    def find_least_likely_word(probability_fcn, probability_dict, word_array) -> str:
        # TODO: interface the parameters or curry whichever is more big brain
        lowest_prob = 0
        least_likely_word = ""
        for word in word_array:
            if (probability := probability_fcn(word, probability_dict)) < lowest_prob:
                least_likely_word = word
                lowest_prob = probability
        return least_likely_word

    def play(self):
        # TODO: be epic with 3.10
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
    file = WORD_FILE_TEMPLATE.format("5")
    sift_words(5, WORD_FILE)
    sift_repetitions(file)
    word_array = load_words(f"unique_{file}")
    letter_prob = calc_letter_prob(word_array)
    letter_prob_by_pos = calc_letter_prob_per_pos(word_array)

    print(find_most_likely_word(calc_word_prob, letter_prob, word_array))
    print(
        find_most_likely_word(calc_word_prob_with_pos, letter_prob_by_pos, word_array)
    )
    print(find_most_likely_word(calc_word_prob_consonant, letter_prob, word_array))
    print(
        find_most_likely_word(
            calc_word_prob_consonant_with_pos, letter_prob_by_pos, word_array
        )
    )


if __name__ == "__main__":
    main()
