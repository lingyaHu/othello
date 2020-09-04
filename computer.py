class Computer:
    def __init__(self, tiles, num, color):
        self.tiles = tiles
        self.num = num
        self.color = color

    def move(self):
        flip_max = 0
        end_point = [0, 0]
        for x in range(self.num):
            for y in range(self.num):
                if self.tiles.flip_count(x, y, self.color) > flip_max:
                    # only if the flip number is more than the max number,
                    # it will update the end point
                    flip_max = self.tiles.flip_count(x, y, self.color)
                    end_point[0] = x
                    end_point[1] = y
        self.tiles.check_move(end_point[0], end_point[1], self.color)
