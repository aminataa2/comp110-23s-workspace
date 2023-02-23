"""One Shot Wordle!"""
__author__: str = "730482498"

secret: str = "python" # secret_word
value: int = len(secret) #bad name
guess: str = input(f"What is your {value}-letter guess? ") # guess_word

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""
anywhere_else: bool = False
correct_counter: int = 0

while (len(guess) != value):
        guess: str = input(f"That was not {value} letters! Try again: ")

while (index < len(secret)):
    alternate: int = 0
    anywhere_else = False
    if (guess[index] == secret[index]):
        emoji = emoji + GREEN_BOX
        correct_counter = correct_counter + 1
    else:
        while (alternate < len(secret)): 
            if (secret[alternate] == guess[index]):
                anywhere_else = True
            alternate = alternate + 1
        if (anywhere_else):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1


print(emoji)
if (guess == secret):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    

