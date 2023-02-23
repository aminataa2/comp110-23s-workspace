"""One Shot Wordle!"""
__author__: str = "730482498"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = ""
anywhere_else: bool = False
alternate: int = 0

while index < len(secret):
    if (guess[index] == secret[index]):
        emoji = emoji + GREEN_BOX
    else:
        while anywhere_else == False and alternate < len(secret):
            if (secret[alternate] == guess[index]):
                anywhere_else = True
            else:
                alternate = alternate + 1
        if anywhere_else == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
print(emoji)


if guess == secret:
    print("Woo! You got it!")
else:
    if len(guess) == 6 and guess != secret:
     print("Not quite. Play again soon!")
    while len(guess) != 6:
        guess: str = input("That was not 6 letters! Try again: ")
        if len(guess) == 6 and guess != secret:
            print("Not quite. Play again soon!")

