"""Single-attempt Wordle game"""
__author__: str = 730614632

secret_word: str = "python"
word: str = input("What is your 6-letter guess? ")

while word != secret_word:
    if len(word) == len(secret_word):
        if word == secret_word:
            print()
    else:
        word = input("That was not 6 letters! Try again: ")

