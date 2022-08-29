"""EX01 - Chardle - Wordle Prototype."""

__author__ = "730614632"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

i: int = 0
count: int = 0
if character == word[i]:
    print(character + " found at index " + str(i))
    count = count + 1
i = i + 1
if character == word[i]:
    print(character + " found at index " + str(i))
    count = count + 1
i = i + 1
if character == word[i]:
    print(character + " found at index " + str(i))
    count = count + 1
i = i + 1
if character == word[i]:
    print(character + " found at index " + str(i))
    count = count + 1
i = i + 1
if character == word[i]:
    print(character + " found at index " + str(i))
    count = count + 1

if count > 1:
    print(str(count) + " instances of " + character + " found in " + word)
if count == 1: 
    print(str(count) + " instance of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)
