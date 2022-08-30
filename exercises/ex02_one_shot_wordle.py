"""Single-attempt Wordle game."""
__author__ = "730614632"

secret_word: str = "python"
secret_length: int = len(secret_word)
word: str = input(f"What is your {secret_length}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != len(secret_word):
    word = input(f"That was not {secret_length} letters! Try again: ")
i: int = 0
sequence: str = ""
if word == secret_word:
    while i < len(secret_word):
        sequence = sequence + "\U0001F7E9"
        i = i + 1
    print(sequence)
    print("Woo! You got it!")
else:
    while i < len(secret_word):
        if word[i] == secret_word[i]:
            sequence = sequence + "\U0001F7E9"
        else:
            position_check: bool = False
            j: int = 0
            while j < len(secret_word):
                if word[i] == secret_word[j]:
                    if position_check is False:
                        sequence = sequence + "\U0001F7E8"
                    position_check = True
                j = j + 1
            if position_check is False:
                sequence = sequence + "\U00002B1C"
        i = i + 1
    print(sequence)
    print("Not quite. Play again soon!")