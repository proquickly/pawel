BOARD_SIZE = 8
SQUARE_SIZE = 600 / BOARD_SIZE



def chess_to_screen_coords(x, y):
    row = 8 - (x // SQUARE_SIZE)
    column = (y // SQUARE_SIZE) + 1
    return int(row), int(column)


def screen_to_chess_coords(x, y):
    row = (BOARD_SIZE * SQUARE_SIZE) - (x * SQUARE_SIZE)
    column = (y * SQUARE_SIZE) - SQUARE_SIZE
    return int(row), int(column)



