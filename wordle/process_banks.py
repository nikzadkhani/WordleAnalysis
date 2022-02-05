#
# process_banks.py
#
# Used to generate new word banks for different wordle strategies/games
#
# TODO:
#  - finish commenting these classes and repath the word_files
#  - think about using dynamic pathing (glob?, that other path library?) instead of static maybe?
#

WORD_FILE = "words_alpha.txt"
WORD_FILE_TEMPLATE = "{}_letter_words.txt"
VOWELS = "aeiouy"


def sift_words(num_letters: int, words_file: str) -> None:
    """ Generate a new file that only has words found in words_file of length
    num_letters.
    :param num_letters: number of letters words should have in new file
    :param words_file: path to the a text file containing the words to sift
    through, it is expected that the words in words_file will be newline 
    seperated
    """
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
