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


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"   
WHITE_BOX: str = "\U00002B1C"

box_string_1: str = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX 
box_string_2: str = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
box_string_3: str = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
box_string_4: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX 

user1: int = int(input("Pick a secret boat location between 1 and 4: "))
user2: int = int(input("Guess a number between 1 and 4: "))
result: str = ""
row_counter: int =+ 1 

while row_counter <= grid:
    emoji_row: str = ""
    if user2 == 1:                    
        if user1 == 1:
            result += RED_BOX
        else:
            result += WHITE_BOX
    else:
        result += BLUE_BOX
    if user2 == 2:
        if user1 == 2:
            result += RED_BOX
        else:
            result += WHITE_BOX
    else:
        result += BLUE_BOX
    if user2 == 3:
        if user1 == 3:
            result += RED_BOX
        else:
            result += WHITE_BOX
    else:
        result += BLUE_BOX
    if user2 == 4:
        if user1 == 4:
            result += RED_BOX
        else:
            result += WHITE_BOX
    else:
        result += BLUE_BOX
    print(result)
    column_counter: int =+ 1
    if guess_row == row_counter:
        while column_counter <= grid:
            if guess_column == column_counter:
                result += RED_BOX or WHITE_BOX
            else:
                result += BLUE_BOX
            column_counter += 1
while column_counter <= grid:
    if guess_column == column_counter:
        result += RED_BOX or WHITE_BOX
    else:
        result += BLUE_BOX
    column_counter += 1
    print(result)
    row_counter += 1