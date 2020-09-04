from computer import Computer


class Board:
    def __init__(self, board_size, space, num, gc, tiles, WHITE, BLACK):
        self.board_size = board_size
        self.space = space
        self.num = num
        self.gc = gc
        self.tiles = tiles
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.COLOR = self.BLACK
        self.TURN = self.BLACK
        self.WAIT_TIME = 120
        self.COUNTER = 0
        self.SPEED = 1

    def display(self):
        background(0, 100, 0)  # Draw the board
        strokeWeight(2)
        # Draw the lines
        for i in range(self.space, self.board_size, self.space):
            line(0, i, self.board_size, i)
            line(i, 0, i, self.board_size)
        # To create the delay time for computer
        if self.TURN == self.WHITE and self.gc.FINISH is False:
            self.COUNTER += self.SPEED
            self.gc.ai_turn = True
        # If the time is up, it's ai's turn to make a move,
        # and the counter will be cleared out.
        if self.COUNTER > self.WAIT_TIME:
            self.gc.ai_turn = False
            self.ai_show()
            self.COUNTER = 0
        self.tiles.display()

    def ai_show(self):
        ai = Computer(self.tiles, self.num, self.TURN)
        ai.move()
        self.check_if_ends()
        self.change_color()
        self.check_if_half_ends()

# If the position user clicks has a legal move, after the move
# we need to check if gameover by counting the numbers of tiles.
# We also need to check if there are legal moves left for the
# other color, if not, check if there are legal moves left for
# this color. If also not, game is also for no legal moves
# remain for each color.
    def user_move(self, mouse_x, mouse_y):
        x = mouse_x // self.space
        y = mouse_y // self.space
        if self.tiles.check_move(x, y, self.COLOR):
            self.check_if_ends()
            self.change_color()
            self.check_if_half_ends()

    def check_if_half_ends(self):
        if not self.tiles.legal_moves_exist(self.COLOR):
            self.change_color()
            if not self.tiles.legal_moves_exist(self.COLOR):
                # There is no legal moves for each color
                self.check_if_ends(True)
        self.TURN = self.COLOR

    def check_if_ends(self, half_ends=False):
        n = self.num * self.num
        black = self.tiles.count(self.BLACK)
        white = self.tiles.count(self.WHITE)
        if black + white == n or half_ends:
            self.gc.black_num = black
            self.gc.white_num = white
            if black > white:
                self.gc.black_wins = True
            elif black < white:
                self.gc.white_wins = True
            else:
                self.gc.tie = True

    def change_color(self):
        if self.COLOR == self.BLACK:
            self.COLOR = self.WHITE
            print("It's computer's turn!")
        else:
            self.COLOR = self.BLACK
            print("It's user's turn!")
