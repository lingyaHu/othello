from tile import Tile


class Tiles:
    def __init__(self, space, num, WHITE, BLACK):
        self.tiles = []
        self.num = num
        self.space = space
        for row in range(num):
            for col in range(num):
                if col == 0:
                    self.tiles.append([])
                self.tiles[row].append(Tile(self.space, row, col, -1))
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.XY_INDEX = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1),
                         (-1, 0), (0, -1), (0, 1)]
        self.tiles[num // 2 - 1][num // 2 - 1].set_color(self.WHITE)
        self.tiles[num // 2 - 1][num // 2].set_color(self.BLACK)
        self.tiles[num // 2][num // 2 - 1].set_color(self.BLACK)
        self.tiles[num // 2][num // 2].set_color(self.WHITE)

    def display(self):
        for i in range(self.num):
            for j in range(self.num):
                if self.tiles[i][j].color != -1:
                    self.tiles[i][j].display()

#   In this method, if there exists tiles which can be flipped around,
#   tiles will be flipped directly during every direction's check.
#   If it will not trigger any tile's flipping around,
#   this is not a legal move for the user
#   and the tile won't be moved to this click position.
    def check_move(self, x, y, color):
        if self.tiles[x][y].color == -1:
            legal = False
            for item in self.XY_INDEX:
                if self.one_line_check(x, y, item[0], item[1], color, True):
                    legal = True
            if legal:
                self.tiles[x][y].set_color(color)
                return True
        return False

#   This method is to check if there exist at least one tile with different
#   color and at least one tile with the same color after that in this line.
#   If this line match the condition, the tiles with different color will be
#   flipped right away.
    def one_line_check(self, x, y, x_add, y_add, old_color, flip):
        i = x + x_add
        j = y + y_add
        if old_color == self.BLACK:
            dif_color = self.WHITE
        else:
            dif_color = self.BLACK
        while self.in_board(i, j) and self.tiles[i][j].color == dif_color:
            i += x_add
            j += y_add
        if self.in_board(i, j) and self.tiles[i][j].color != -1:
            if i != x + x_add or j != y + y_add:
                if flip:
                    self.flip_color(x, y, i, j, old_color)
                return True
        return False

    def in_board(self, i, j):
        return i >= 0 and j >= 0 and i < self.num and j < self.num

#   This method is just to check if there is a position around which
#   at least one tile can be flipped.
    def legal_moves_exist(self, color):
        for x in range(self.num):
            for y in range(self.num):
                if self.tiles[x][y].color == -1:
                    for i in self.XY_INDEX:
                        if self.one_line_check(x, y, i[0], i[1], color, False):
                            return True
        return False

    def flip_color(self, x, y, end_x, end_y, color):
        i = x
        j = y
        while i != end_x or j != end_y:
            if end_x > i:
                i += 1
            elif end_x < i:
                i -= 1
            if end_y > j:
                j += 1
            elif end_y < j:
                j -= 1
            self.tiles[i][j].set_color(color)

    def count(self, color):
        n = 0
        for i in range(self.num):
            for j in range(self.num):
                if self.tiles[i][j].color == color:
                    n += 1
        return n

#   This method is designed for the computer move.
#   It will count the potential tiles that can be flipped
#   around the specific position.
    def flip_count(self, x, y, color):
        if color == self.BLACK:
            dif_color = self.WHITE
        else:
            dif_color = self.BLACK
        flip_num = 0
        if self.tiles[x][y].color == -1:
            for item in self.XY_INDEX:
                if self.one_line_check(x, y, item[0], item[1], color, False):
                    i = x + item[0]
                    j = y + item[1]
                    while (self.in_board(i, j) and
                           self.tiles[i][j].color == dif_color):
                        i += item[0]
                        j += item[1]
                        flip_num += 1
        return flip_num
