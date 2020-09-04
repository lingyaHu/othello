import unittest
from tiles import Tiles
from tile import Tile


class TestTiles(unittest.TestCase):
    def test_constructor(self):
        t = Tiles(100, 8, 255, 0)
        self.assertEqual(t.space, 100)
        self.assertEqual(t.num, 8)
        self.assertEqual(t.WHITE, 255)
        self.assertEqual(t.BLACK, 0)
        t_list = []
        for row in range(t.num):
            for col in range(t.num):
                if col == 0:
                    t_list.append([])
                t_list[row].append(Tile(t.space, row, col, -1))
        t_list[t.num // 2 - 1][t.num // 2 - 1].set_color(t.WHITE)
        t_list[t.num // 2 - 1][t.num // 2].set_color(t.BLACK)
        t_list[t.num // 2][t.num // 2 - 1].set_color(t.BLACK)
        t_list[t.num // 2][t.num // 2].set_color(t.WHITE)

        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color,
                         t_list[t.num // 2 - 1][t.num // 2 - 1].color)
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2].color,
                         t_list[t.num // 2 - 1][t.num // 2].color)
        self.assertEqual(t.tiles[t.num // 2][t.num // 2 - 1].color,
                         t_list[t.num // 2][t.num // 2 - 1].color)
        self.assertEqual(t.tiles[t.num // 2][t.num // 2].color,
                         t_list[t.num // 2][t.num // 2].color)

    def test_check_move(self):
        t = Tiles(100, 8, 255, 0)
        # Take a illegal move on the left-top corner.
        self.assertEqual(t.tiles[0][0].color, -1)
        self.assertFalse(t.check_move(0, 0, 255))
        self.assertEqual(t.tiles[0][0].color, -1)

        # Take a legal move around the middle default white chess,
        # and the blank tile will show a black chess.
        # Meanwhile the white chess will become black.
        self.assertEqual(t.tiles[t.num // 2 - 2][t.num // 2 - 1].color, -1)
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 255)

        self.assertTrue(t.check_move(t.num // 2 - 2, t.num // 2 - 1, 0))

        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 0)
        self.assertEqual(t.tiles[t.num // 2 - 2][t.num // 2 - 1].color, 0)

    def test_one_line_check(self):
        t = Tiles(100, 8, 255, 0)
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 255)
        self.assertTrue(t.one_line_check(t.num // 2 - 2,
                                         t.num // 2 - 1, 1, 0, 0, False))
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 255)
        self.assertTrue(t.one_line_check(t.num // 2 - 2,
                                         t.num // 2 - 1, 1, 0, 0, True))
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 0)

    def test_in_board(self):
        t = Tiles(100, 8, 255, 0)
        self.assertFalse(t.in_board(-1, 0))
        self.assertTrue(t.in_board(0, 0))
        self.assertFalse(t.in_board(9, 0))

    def test_flip_color(self):
        t = Tiles(100, 8, 255, 0)
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 255)
        t.flip_color(t.num // 2 - 2, t.num // 2 - 1, t.num // 2 - 1,
                     t.num // 2 - 1, 0)
        self.assertEqual(t.tiles[t.num // 2 - 1][t.num // 2 - 1].color, 0)

    def test_legal_moves_exist(self):
        t = Tiles(100, 8, 255, 0)
        # At the beginning, for each color, there exist legal moves.
        self.assertTrue(t.legal_moves_exist(255))
        self.assertTrue(t.legal_moves_exist(0))

    def test_flip_count(self):
        t = Tiles(100, 8, 255, 0)
        self.assertEqual(t.flip_count(t.num // 2 - 2, t.num // 2 - 1, 0), 1)
        self.assertEqual(t.flip_count(0, 0, 0), 0)

    def test_count(self):
        t = Tiles(100, 8, 255, 0)
        self.assertEqual(t.count(0), 2)
        self.assertEqual(t.count(255), 2)


if __name__ == '__main__':
    unittest.main()
