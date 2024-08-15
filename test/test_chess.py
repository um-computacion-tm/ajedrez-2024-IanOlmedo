import unittest
from chess import Chess

class ChessTest(unittest.TestCase):
    def test_init(self):
        chess = Chess()
        self.assertEqual(chess.__board__.__positions__, [[None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None],
                                                        [None, None, None, None, None, None, None, None]])
        self.assertEqual(chess.__turn__, "white")

