import unittest
from ajedrez.queen import Queen
from ajedrez.board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__queen__ = Queen("WHITE", "QUEEN")


    def test_movimiento_queen_invalido(self):
        self.__board__.set_piece(6, 4, self.__queen__)
        movimiento = self.__queen__.mover_a(self.__board__, 6, 4, 7, 4)

        self.assertIsNone (movimiento)

    def test_mover_queen_a(self):
        self.__board__.set_piece(4, 4, self.__queen__)
        reina_negra = Queen("BLACK", "QUEEN")
        self.__board__.set_piece(1, 4, reina_negra)
        self.__queen__.mover_a(self.__board__, 4, 4, 1, 4)
        self.assertEqual(self.__board__.get_piece(1,4), self.__queen__)
        self.assertIsNone(self.__board__.get_piece(4,4))

if __name__ == "__main__":
    unittest.main()

