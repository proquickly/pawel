# BOARD_SIZE = 600
BOARD_SIZE = 480
SQUARE_SIZE = BOARD_SIZE // 8


def translate_number_to_sequence(num):
    sequence_value = 8 - (num * 8 // BOARD_SIZE)
    return sequence_value


# Test the function
"""print(translate_number_to_sequence(0))  # Should output 8
print(translate_number_to_sequence(60))  # Should output 7
print(translate_number_to_sequence(120))  # Should output 6
print(translate_number_to_sequence(180))  # Should output 5
print(translate_number_to_sequence(240))  # Should output 4
print(translate_number_to_sequence(300))  # Should output 3
print(translate_number_to_sequence(360))  # Should output 2
print(translate_number_to_sequence(420))  # Should output 1
print("---")"""


def translate_sequence_to_number(seq):
    number_value = (8 - seq) * BOARD_SIZE // 8
    return number_value


# Test the function
"""print(translate_sequence_to_number(8))  # Should output 0
print(translate_sequence_to_number(7))  # Should output 60
print(translate_sequence_to_number(6))  # Should output 120
print(translate_sequence_to_number(5))  # Should output 180
print(translate_sequence_to_number(4))  # Should output 240
print(translate_sequence_to_number(3))  # Should output 300
print(translate_sequence_to_number(2))  # Should output 360
print(translate_sequence_to_number(1))  # Should output 420
print("---")"""


def screen_to_board(row, column):
    if row in (0, 420):
        return (
            translate_number_to_sequence(row),
            int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1),
        )
    return (
        translate_number_to_sequence(row),
        int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1) - 3,
    )


def board_to_screen(row, column):
    if row in (0,420):
        return translate_sequence_to_number(row), int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1)
    return translate_sequence_to_number(row), int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1) - 3


"""print(screen_to_board(0, 0))
assert screen_to_board(0, 0) == (8, 1)
print(screen_to_board(420, 420))
assert screen_to_board(420, 420) == (1, 8)
print(screen_to_board(60, 60))
assert screen_to_board(60, 60) == (7, 2)
print(screen_to_board(180, 180))
assert screen_to_board(180, 180) == (5, 4)
print(screen_to_board(120, 180))
assert screen_to_board(120, 180) == (6, 4)"""

"""print(board_to_screen(1, 8))
#assert board_to_screen(1, 8) == (420, 420)
print(board_to_screen(8, 8))
assert board_to_screen(8, 8) == (0, 420)"""
