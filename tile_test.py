import unittest
from tile import Tile


class TestTiles(unittest.TestCase):
    def test_constructor(self):
        tile = Tile(100, 2, 3, 255)
        self.assertEqual(tile.col, 2)
        self.assertEqual(tile.row, 3)
        self.assertEqual(tile.color, 255)
        self.assertEqual(tile.size, 100)
        self.assertEqual(tile.RATIO, 0.9)

    def test_set_color(self):
        tile = Tile(100, 2, 3, 255)
        self.assertEqual(tile.color, 255)
        tile.set_color(0)
        self.assertEqual(tile.color, 0)


if __name__ == '__main__':
    unittest.main()
