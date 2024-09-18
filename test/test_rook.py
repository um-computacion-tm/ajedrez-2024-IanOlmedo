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

    def test_rook_mover_a(self):
        self.__board__.set_piece(0, 3, self.__rook__)
        posicion = self.__rook__.mover_a(self.__board__, 5,0 , 3, 2)
        self.assertEqual(posicion, self.__board__.get_piece(3, 2))

    def test_rook_mover_a2(self):
        self.__board__.set_piece(4,4, self.__rook__)
        self.__board__.set_piece(3,4, Rook("BLACK"))
        self.assertEqual(self.__rook__.mover_a(self.__board__, 4, 4, 5, 4), self.__board__.get_piece(5, 4))
        self.assertEqual(self.__board__.get_piece(5,4), self.__rook__)
        self.assertIsNone(self.__board__.get_piece(4,4))


if __name__ == '__main__':
    unittest.main()


