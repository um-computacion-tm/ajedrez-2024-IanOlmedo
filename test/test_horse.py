import unittest
from ajedrez.board import Board
from ajedrez.horse import Horse
from ajedrez.pawn import Pawn
from ajedrez.queen import Queen

class TestHorse(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__horse__ = Horse("WHITE")

    def test_mover_horse_a(self):
        self.__board__.set_piece(3,5, self.__horse__)
        reina_negra = Queen("BLACK")
        self.__board__.set_piece(1,4, reina_negra)
        self.__horse__.mover_a_h(self.__board__, 3, 5, 1, 4)
        self.assertEqual(self.__board__.get_piece(1,4), self.__horse__)
        self.assertIsNone(self.__board__.get_piece(3,5))

    def test_get_moves_horse(self):
        # Posición inicial del caballo
        self.__board__.set_piece(7, 6, self.__horse__)
        expected_moves = [(5, 5), (5, 7)]
        self.assertEqual(self.__horse__.get_moves_horse(self.__board__, 7, 6), expected_moves)

        # Centro del tablero
        self.__board__.set_piece(3, 6, self.__horse__)
        expected_moves_center = [(1, 5), (1, 7), (2, 4), (4, 4), (5, 5), (5, 7)]
        self.assertEqual(sorted(self.__horse__.get_moves_horse(self.__board__, 3, 6)), sorted(expected_moves_center))

    def test_movimiento_horse_invalido(self):
        self.__board__.set_piece(6, 4, self.__horse__)
        movimiento = self.__horse__.mover_a_h(self.__board__, 7, 1, 8, 3)

        self.assertIsNone (movimiento)




if __name__ == '__main__':
    unittest.main()

