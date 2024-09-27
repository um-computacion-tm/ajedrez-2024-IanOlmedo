import unittest
from ajedrez.piezas import Piece
from ajedrez.board import Board
from ajedrez.rook import Rook

class RookTest(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE", "ROOK")



    def test_str_rook(self):
        self.assertEqual(str(self.__rook__), "♖")



if __name__ == '__main__':
    unittest.main()



