"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730482498"

five_word: str = input("Enter a 5-character word: ")
if ((len(five_word)) == 5):
    single_character: str = input("Enter a single character: ")
else:
    print  ("Error: Word must contain 5 characters")
    exit()

if ((len(single_character)) == 1):
    match_characters: int = 0
    print("Searching for " + single_character + " in " + five_word)
else:
    print("Error: Character must be a single character.")
    exit()


if (single_character == five_word[0]):
    print  (single_character + " found at index 0")
    match_characters = match_characters + 1

if (single_character == five_word[1]):
    print  (single_character + " found at index 1")
    match_characters = match_characters + 1

if (single_character == five_word[2]):
    print  (single_character + " found at index 2")
    match_characters = match_characters + 1

if (single_character == five_word[3]):
    print  (single_character + " found at index 3")
    match_characters = match_characters + 1

if (single_character == five_word[4]):
    print  (single_character + " found at index 4")
    match_characters = match_characters + 1

if (match_characters == 0):
    print  ("No instances of " + single_character + " found in " + five_word)

if (match_characters == 1):
    print  ("1 instance of " + single_character + " found in " + five_word)

if (match_characters == 2):
    print  ("2 instances of " + single_character + " found in " + five_word)

if (match_characters == 3):
    print  ("3 instances of " + single_character + " found in " + five_word)

if (match_characters == 4):
    print  ("4 instances of " + single_character + " found in " + five_word)

if (match_characters == 5):
    print  ("5 instances of " + single_character + " found in " + five_word)
