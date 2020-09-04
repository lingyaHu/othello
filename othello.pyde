from board import Board
from tiles import Tiles
from game_controller import GameController
from computer import Computer

SIZE = 600
CELL_NUM = 8
CELL_LENGTH = SIZE // CELL_NUM
WHITE = 255
BLACK = 0

gc = GameController(SIZE)
tiles = Tiles(CELL_LENGTH, CELL_NUM, WHITE, BLACK)
board = Board(SIZE, CELL_LENGTH, CELL_NUM, gc, tiles, WHITE, BLACK)

def setup():
    size(SIZE,SIZE)

def draw():
    if gc.FINISH == True:
        gc.record()
    board.display()
    gc.update()
    if gc.stop:
        noLoop()

def mousePressed():
    if board.TURN == board.BLACK:
        board.user_move(mouseX, mouseY)
