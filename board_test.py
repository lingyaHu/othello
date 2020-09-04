import unittest
from board import Board
from game_controller import GameController
from tiles import Tiles


class TestBoard(unittest.TestCase):
    def test_constructor(self):
        gc = GameController(600)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(600, 100, 8, gc, tiles, 255, 0)
        self.assertEqual(b.board_size, 600)
        self.assertEqual(b.space, 100)
        self.assertEqual(b.num, 8)
        self.assertEqual(b.gc, gc)
        self.assertEqual(b.tiles, tiles)
        self.assertEqual(b.WHITE, 255)
        self.assertEqual(b.BLACK, 0)

    def test_ai_show(self):
        gc = GameController(800)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(800, 100, 8, gc, tiles, 255, 0)
        self.assertEqual(b.tiles.count(b.WHITE), 2)
        b.TURN = b.WHITE  # Switch the color, let ai makes move
        b.ai_show()
        self.assertEqual(b.tiles.count(b.WHITE), 4)

    def test_user_move(self):
        gc = GameController(800)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(800, 100, 8, gc, tiles, 255, 0)
        self.assertEqual(b.tiles.tiles[2][3].color, -1)
        b.user_move(250, 320)
        self.assertEqual(b.tiles.tiles[2][3].color, 0)

    def test_check_if_half_ends(self):
        gc = GameController(600)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(600, 100, 8, gc, tiles, 255, 0)
        b.check_if_half_ends()
        self.assertFalse(gc.black_wins)
        b.tiles.tiles[3][3].set_color(b.BLACK)
        b.tiles.tiles[4][4].set_color(b.BLACK)
        b.check_if_half_ends()
        self.assertTrue(gc.black_wins)

    def test_check_if_ends(self):
        gc = GameController(600)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(600, 100, 8, gc, tiles, 255, 0)
        self.assertFalse(gc.tie)
        b.check_if_ends()
        self.assertFalse(gc.tie)
        b.check_if_ends(True)
        self.assertTrue(gc.tie)

    def test_change_color(self):
        gc = GameController(600)
        tiles = Tiles(100, 8, 255, 0)
        b = Board(600, 100, 8, gc, tiles, 255, 0)
        self.assertEqual(b.COLOR, 0)
        b.change_color()
        self.assertEqual(b.COLOR, 255)


if __name__ == '__main__':
    unittest.main()
