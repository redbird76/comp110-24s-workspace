"""EX02 - One Shot Battleship"""

__author__: 730563209

grid = 4
secret_row = 3
secret_column = 2
guess_row: int = int(input("Guess a row: "))

while guess_row > grid or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))

guess_column: int = int(input("Guess a column: "))
while guess_column > grid or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid} by {grid}. Try again: "))



BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"   
WHITE_BOX: str = "\U00002B1C"

if guess_row == secret_row and guess_column == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX 



row_counter: int = 1 
column_counter: int = 1
while row_counter <= grid:
    emoji_row: str = ""
    column_counter = 1
    while column_counter <= grid:
        if guess_column == column_counter and guess_row == row_counter:
            emoji_row += result
        else:
            emoji_row += BLUE_BOX
        column_counter += 1
    print(emoji_row)   
    row_counter += 1 

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row != secret_row:
    print("Close! Correct column, wrong row.")
elif guess_column != secret_column:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!") 