"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while correct == False: # same thing as saying while not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if guess < SECRET:
            print(f"{guess} too low!")
        if guess > SECRET:
            print(f"{guess} too high!")
        print("Try again!")