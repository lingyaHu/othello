class Tile:
    def __init__(self, space, col, row, tile_color):
        self.col = col
        self.row = row
        self.color = tile_color
        self.size = space
        self.RATIO = 0.9

    def display(self):
        """Draws the tile"""
        strokeWeight(2)
        fill(self.color)
        size = self.size
        col = self.col * size + size / 2
        row = self.row * size + size / 2
        ellipse(col, row, size * self.RATIO, size * self.RATIO)

    def set_color(self, new_color):
        self.color = new_color
