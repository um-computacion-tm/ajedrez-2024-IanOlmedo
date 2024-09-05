

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

    def test_size(self):
        cantidadcasillas = 8
        self.assertEqual(self.board.get_size(), cantidadcasillas)






    def test_move_knight(self):
        # Mover caballo blanco de (7, 1) a (5, 2)
        moved_piece = self.board.move(7, 1, 5, 2)
        self.assertIsInstance(moved_piece, Horse)
        self.assertEqual(self.board.get_piece(5, 2), moved_piece)
        self.assertIsNone(self.board.get_piece(7, 1))


    def test_move_pawn(self):
        # Mover peón blanco de (6, 0) a (4, 0)
        self.pawn = Pawn("WHITE")
        self.board.set_piece(6, 0, self.pawn)
        moved_piece = self.board.move(6, 0, 4, 0)
        self.assertIsInstance(moved_piece, Pawn)
        self.assertEqual(self.board.get_piece(4, 0), moved_piece)
        self.assertIsNone(self.board.get_piece(6, 0))

    def test_invalid_move(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(ValueError):
            self.board.move(2, 2, 3, 3)

        # Intentar mover una pieza a una posición inválida (movimiento no permitido)
        invalid_move = self.board.move(7, 1, 7, 3)  # Caballo no puede moverse así
        self.assertIsNone(invalid_move)

if __name__ == '__main__':
    unittest.main()

"""    def test_move_rook(self):
        # Mover torre blanca de (7, 0) a (5, 0)
        moved_piece = self.board.move(7, 0, 5, 0)
        self.assertIsInstance(moved_piece, Rook)
        self.assertEqual(self.board.get_piece(5, 0), moved_piece)
        self.assertIsNone(self.board.get_piece(7, 0))
    def test_move_bishop(self):
        # Mover alfil blanco de (7, 2) a (5, 0)
        moved_piece = self.board.move(7, 2, 5, 0)
        self.assertIsInstance(moved_piece, Bishop)
        self.assertEqual(self.board.get_piece(5, 0), moved_piece)
        self.assertIsNone(self.board.get_piece(7, 2))
    def test_move_king(self):
        # Mover rey blanco de (7, 4) a (6, 4)
        self.king = King("WHITE")
        self.board.set_piece(2, 2, self.king)
        moved_piece = self.board.move(2, 2, 1, 1)
        self.assertIsInstance(moved_piece, King)
        self.assertEqual(self.board.get_piece(6, 4), moved_piece)
        self.assertIsNone(self.board.get_piece(7, 4))

    def test_move_queen(self):
        # Mover reina blanca de (7, 3) a (6, 3)
        self.queen = Queen("WHITE")
        self.board.set_piece(4,4, self.queen)
        moved_piece = self.board.move(4, 4, 2, 4)
        self.assertIsInstance(moved_piece, Queen)
        self.assertEqual(self.board.get_piece(6, 3), moved_piece)
        self.assertIsNone(self.board.get_piece(7, 3))
"""


