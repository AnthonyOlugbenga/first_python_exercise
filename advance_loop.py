# Advanced Loops

"""
Create a function that takes in two parameters: rows, and columns, 
both of which are integers. The function should draw a playing board

"""
def draw_playing_board(rows, columns):
    if columns <= 90:
    	
        for row in range(int(rows)):
            if row % 2 == 0:
                for col in range(1, int(columns)):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
# After drawing the board, function should return TRUE

        return True
    else:
# For value greater than maximum, function should returns FALSE
        return False


board = draw_playing_board(5, 90)
print(board)