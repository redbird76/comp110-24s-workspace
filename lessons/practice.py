
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"   
WHITE_BOX: str = "\U00002B1C"

def print_grid(size_grid: int, guess_row: int, guess_column: int, guess_correct: bool) -> None:
    if guess_correct:
     result:str = RED_BOX
    else:
        result:str = WHITE_BOX 
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
        row_counter += 1 
        print(emoji_row)

