from wordle.words.word_bank import WordBank
from wordle.constants import LetterState

# fdo
x = [("f", LetterState.GREEN), ("o", LetterState.YELLOW), ("o", LetterState.GREY)]

print(WordBank.is_possible_word("fdo", x))
