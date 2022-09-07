"""EX03 - 6 attempt wordle."""
__author__ = 730614632

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char (word, char) -> bool: 
    """Return True if word contains char."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False

def emojified (guess, secret) -> str:
    """Return emojis for correct character in secret."""
    assert len(guess) == len(secret)
    i: int = 0
    sequence: str = ""
    while i < len(secret):
        emoji: bool = contains_char (secret, guess[i])
        if secret[i] == guess[i]:
            sequence += "\U0001F7E9"
        elif emoji == True:
            sequence += "\U0001F7E8"
        else:
            sequence += "\U00002B1C"
        i += 1
    return sequence

def input_guess (length) -> str:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess

def main () -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    end: bool = False 
    while end == False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            end = True

if __name__ == "__main__":
    main()