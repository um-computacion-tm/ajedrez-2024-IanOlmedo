import unittest
from ajedrez.board import Board
from ajedrez.king import King
from ajedrez.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__king__ = King("WHITE")

    def test_king_moves(self):
        # Centro del tablero
        self.__board__.set_piece(4, 4, self.__king__)
        expected_moves = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

        # Esquina del tablero
        self.__board__.set_piece(0, 0, self.__king__)
        expected_moves_corner = [(0, 1), (1, 0), (1, 1)]
        actual_moves_corner = self.__king__.get_moves_king(self.__board__, 0, 0)
        self.assertEqual(sorted(actual_moves_corner), sorted(expected_moves_corner))

    def test_king_moves_con_obstaculos(self):
        self.__board__.set_piece(4, 4, self.__king__)

        # Piezas aliadas
        self.__board__.set_piece(3, 4, Pawn("WHITE"))
        self.__board__.set_piece(5, 4, Pawn("WHITE"))

        # Piezas enemigas
        self.__board__.set_piece(4, 3, Pawn("BLACK"))
        self.__board__.set_piece(5, 5, Pawn("BLACK"))

        expected_moves = [(3, 3), (3, 5), (4, 3), (4, 5), (5, 3), (5, 5)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_king_mover_a(self):
        self.__board__.set_piece(2, 4, self.__king__)
        self.__king__.mover_a(self.__board__, 2, 4, 1,3)
        self.assertEqual(self.__board__.get_piece(1, 3), self.__king__)
        self.assertIsNone(self.__board__.get_piece(2, 4))

    def test_movimiento_king_invalido(self):
        self.__board__.set_piece(6, 4, self.__king__)
        movimiento = self.__king__.mover_a(self.__board__, 7, 4, 7, 5)

        self.assertIsNone (movimiento)

if __name__ == '__main__':
    unittest.main()
