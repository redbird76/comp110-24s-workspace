grid = 4
secret_row = 3
secret_column = 2
guess_row: int = int(input("Guess a row: "))




while guess_row > grid or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))

guess_column: int = int(input("Guess a column: "))
while guess_column > grid or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid} by {grid}. Try again: "))
   
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")