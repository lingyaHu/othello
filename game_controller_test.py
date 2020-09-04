import unittest
from game_controller import GameController


class TestBoard(unittest.TestCase):
    def test_constructor(self):
        gc = GameController(600)
        self.assertEqual(gc.size, 600)
        self.assertFalse(gc.black_wins)
        self.assertFalse(gc.white_wins)
        self.assertFalse(gc.tie)
        self.assertFalse(gc.stop)
        self.assertEqual(gc.black_num, 0)
        self.assertEqual(gc.white_num, 0)
        self.assertFalse(gc.FINISH)
        self.assertFalse(gc.ai_turn)


if __name__ == '__main__':
    unittest.main()
