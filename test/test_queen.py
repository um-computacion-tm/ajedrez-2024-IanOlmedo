import unittest
from ajedrez.queen import Queen
from ajedrez.board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__queen__ = Queen("WHITE")

    def test_mover_a(self):

        self.__board__.set_piece(4, 4, self.__queen__)
        self.__queen__.mover_a_q(self.__board__, 4, 4, 5, 5)
        self.assertEqual(self.__board__.get_piece(5, 5), self.__queen__)
        self.assertIsNone(self.__board__.get_piece(4, 4))

    def test_movimiento_queen_invalido(self):
        self.__board__.set_piece(6, 4, self.__queen__)
        movimiento = self.__queen__.mover_a_q(self.__board__, 6, 4, 7, 4)

        self.assertIsNone (movimiento)

if __name__ == "__main__":
    unittest.main()

