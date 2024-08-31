import unittest
from ajedrez.rook import Rook
from ajedrez.board import Board

class RookTest(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE")
        self.__board__.set_piece(0, 0, self.__rook__)

    def test_str(self):
        self.assertEqual(str(self.__rook__), "♖")

if __name__ == '__main__':
    unittest.main()


