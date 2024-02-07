"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730563209"


user1: int = int(input("Pick a secret boat location between 1 and 4: "))
if user1 < 1:
    print(f"Error! {user1} too low!")
    exit()
if user1 > 4:
    print(f"Error! {user1} too high!")
    exit()

user2: int = int(input("Guess a number between 1 and 4: "))
if user2 < 1:
    print(f"Error! {user2} too low!")
    exit()
if user2 > 4:
    print(f"Error! {user2} too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C" 

box_string_1: str = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX 
box_string_2: str = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
box_string_3: str = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
box_string_4: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX 

result: str = ""
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

if user2 == user1:
    print("Correct! You hit the ship.")   
else:
    print("Incorrect! You missed the ship.")
