import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from ajedrez.board import Board
from ajedrez.rook import Rook
from ajedrez.horse import Horse
from ajedrez.bishop import Bishop
from ajedrez.queen import Queen
from ajedrez.king import King
from ajedrez.pawn import Pawn

class TestBoard(unittest.TestCase):
    #inicializa el tablero
    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        # se fija si las piezas estan en sus posiciones iniciales
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)


        self.assertIsInstance(self.board.get_piece(0, 1), Horse)
        self.assertIsInstance(self.board.get_piece(0, 6), Horse)
        self.assertIsInstance(self.board.get_piece(7, 1), Horse)
        self.assertIsInstance(self.board.get_piece(7, 6), Horse)


        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)


        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)

        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(7, 4), King)

        for i in range(8):
            self.assertIsInstance(self.board.get_piece(1, i), Pawn)
            self.assertIsInstance(self.board.get_piece(6, i), Pawn)

    def test_empty_squares(self):
        # se fija si las casillas none es donde no hay piezas
        for i in range(2, 6):
            for j in range(8):
                self.assertIsNone(self.board.get_piece(i, j))

    def test_initial_positions(self):
        expected_positions = [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],  # Filas iniciales para piezas negras
            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],  # Peones negros
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],  # Peones blancos
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]   # Filas iniciales para piezas blancas
        ]

        actual_positions = []
        for row in range(8):
            actual_row = []
            for col in range(8):
                piece = self.board.get_piece(row, col)
                actual_row.append(str(piece) if piece else None)
            actual_positions.append(actual_row)


        
        self.assertEqual(actual_positions, expected_positions)

    def test_str_representation(self):
        expected_str = (
            "♜♞♝♛♚♝♞♜\n"
            "♟♟♟♟♟♟♟♟\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n"
            "♖♘♗♕♔♗♘♖\n"
        )
        self.assertEqual(str(self.board), expected_str)


if __name__ == '__main__':
    unittest.main()




