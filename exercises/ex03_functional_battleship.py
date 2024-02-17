"""Functional Battleship."""

__author__: "9"
import random

def input_guess(size: int, location: str) -> int:
    assert location == "row" or location == "column"
    if location == "row":
        guess: int = int(input("Guess a row: "))
        while guess > size or guess < 1:
            guess = int(input(f"The grid is only {size} by {size}. Try again: "))
    else:
        guess: int = int(input("Guess a column: "))
        while guess > size or guess < 1:
            guess = int(input(f"The grid is only {size} by {size}. Try again: "))
    return guess

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"   
WHITE_BOX: str = "\U00002B1C"

def print_grid(size_grid: int, guess_row: int, guess_column: int, guess_correct: bool):
    if guess_correct:
        result: str = RED_BOX
    else:
        result: str = WHITE_BOX 
    row_counter: int = 1 
    column_counter: int = 1
    while row_counter <= size_grid:
        emoji_row: str = ""
        if row_counter == guess_row:
            column_counter = 1
            while column_counter <= size_grid:
                if column_counter == guess_column:
                    emoji_row += result
                else:
                    emoji_row += BLUE_BOX
                column_counter += 1
        else:
            column_counter = 1
            while column_counter <= size_grid:
                emoji_row += BLUE_BOX
                column_counter += 1
        row_counter += 1 
        print(emoji_row)

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: bool) -> bool:
    if secret_row == guess_row and secret_column == guess_column:
        return(True)
    else:
        return(False)

def main(grid_size: int, secret_row: int, secret_column: int):
    turn = 0
    max_turns = 5
    won_game = False
    while turn <= max_turns and won_game == False:
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct: int = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            won_game = True
        else:
            print("Miss!")
        if turn == max_turns:
            print(f"X/{max_turns} - Better luck next time!")
            quit()
if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))   