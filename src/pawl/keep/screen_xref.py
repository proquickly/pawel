BOARD_PIXELS = 480, 480
ROW_PIXELS = BOARD_PIXELS[0] // 8
COLUMN_PIXELS = BOARD_PIXELS[1] // 8


def board_to_screen(row, column):
    row = (row - 1) * ROW_PIXELS
    column = (column - 1) * COLUMN_PIXELS
    return row, column


def screen_to_board(row, column):
    row = row // ROW_PIXELS
    column = column // COLUMN_PIXELS
    return row, column
