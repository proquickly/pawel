import pygame
import sys
import random
import new_oochesss as new_chess
import pysnooper
import translate_coordinates
import gpt_version2

pygame.init()

BOARD_SIZE = 8
SQUARE_SIZE = 60
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480

WHITE = (255, 255, 255)
LIGHT_BROWN = (160, 82, 45)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

BOARD_PIXELS = 480, 480
ROW_PIXELS = BOARD_PIXELS[0] // 8
COLUMN_PIXELS = BOARD_PIXELS[1] // 8

BOARD_PIXELS = 600, 600
ROW_PIXELS = BOARD_PIXELS[0] // 8
COLUMN_PIXELS = BOARD_PIXELS[1] // 8

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Chess Game')

current_turn = 'w'
selected_piece = None
selected_position = (0, 0)
king_moved = {'w': False, 'b': False}
rook_moved = {'w': {'left': False, 'right': False}, 'b': {'left': False, 'right': False}}

def load_images():
    pieces = ['K', 'Q', 'B', 'N', 'R', 'p']
    colors = ['w', 'b']
    images = {}
    for piece in pieces:
        for color in colors:
            imageName = f"{color}{piece}.png"
            image = pygame.image.load(imageName).convert_alpha()
            images[f"{color}{piece}"] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    return images

def draw_board(screen):
    colors = [WHITE, LIGHT_BROWN]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def board_for_draw():
    """need to fix mapping screen coordinates to positions to lists of lists below"""
    return [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
    ]

#@pysnooper.snoop()
def draw_pieces(screen, images, board):
    for row in range(BOARD_SIZE - 1, -1, -1): # 
        for col in range(BOARD_SIZE - 1, -1, -1): # 
            piece = board.board[(row+1,col+1)]
            row, col = board_to_screen(row,col)
            piece = convert_to_pygame(piece, board)

            if piece:
                screen.blit(piece, pygame.Rect(col, row, SQUARE_SIZE, SQUARE_SIZE))

def convert_to_pygame(piece, board):
    return pygame.surface.Surface((SQUARE_SIZE,SQUARE_SIZE))#board.display_pieces[piece]FIXME: 

#@pysnooper.snoop()
def handle_mouse_event(event_pos, game):
    global current_turn, selected_piece, selected_position
    row, col = translate_coordinates.chess_to_screen_coords(event_pos[0], event_pos[1])# FIXME: the problem is board slicing. so for example when i click square with the 'wR' the coordinates will be (1,1) and to the slicing it will be 'bR' 
    
    print(f"Clicked position: Screen ({event_pos[0]}, {event_pos[1]}) -> Board ({row}, {col})")

    if selected_piece is None:
        if game.board([row,col]) is not None and game.board([row,col])[0] == current_turn:#FIXME: fix the [0]  
            selected_piece = game.board[(row,col)]
            selected_position = (row, col)
            print(f"Selected piece: {selected_piece} at {selected_position}")
    else:
        print(f"Deselected piece: {selected_piece} from {selected_position}")
        selected_piece = None

def board_to_screen(row, column):
    row = (BOARD_SIZE - row) * SQUARE_SIZE
    column = (column - 1) * SQUARE_SIZE
    return row, column

#idea: 1
"""def screen_to_board(x, y):
    #row = x // SQUARE_SIZE + 8
    #col = ((WINDOW_HEIGHT - (y*60)) // SQUARE_SIZE) - 7
    #row = 9 - ((x + 60) // SQUARE_SIZE)
    #col = ((WINDOW_HEIGHT - y) // SQUARE_SIZE) - 7

    col = int(round(x // SQUARE_SIZE + 1,0))
    row = int(round(8 - (y // SQUARE_SIZE),0))
    return row, col"""

#idea: 2
"""def screen_to_board(x, y):
    column = (x // SQUARE_SIZE) + 1
    row = BOARD_SIZE - (y // SQUARE_SIZE)
    return row, column"""

#idea: 3
"""def screen_to_board(x, y):
    column = 1
    while x >= SQUARE_SIZE:
        x -= SQUARE_SIZE
        column += 1

    row = BOARD_SIZE
    while y >= SQUARE_SIZE:
        y -= SQUARE_SIZE
        row -= 1

    return row, column"""

def screen_to_board(row, column):
    if row in (0, 420):
        return (
            gpt_version2.translate_number_to_sequence(row),
            int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1),
        )
    return (
        gpt_version2.translate_number_to_sequence(row),
        int(8 - (BOARD_SIZE / (column + SQUARE_SIZE)) + 1) - 3,
    )

def play_game():
    clock = pygame.time.Clock()
    images = load_images()
    game = new_chess.Game.build_game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_event(event.pos, game)
        screen.fill((0, 0, 0))
        draw_board(screen)
        draw_pieces(screen, images, game)
        pygame.display.flip()
        clock.tick(60)



