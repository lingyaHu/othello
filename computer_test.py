import unittest
from computer import Computer
from tiles import Tiles


class TestBoard(unittest.TestCase):
    def test_constructor(self):
        tiles = Tiles(100, 8, 255, 0)
        c = Computer(tiles, 8, 255)
        self.assertEqual(c.tiles, tiles)
        self.assertEqual(c.num, 8)
        self.assertEqual(c.color, 255)


if __name__ == '__main__':
    unittest.main()
