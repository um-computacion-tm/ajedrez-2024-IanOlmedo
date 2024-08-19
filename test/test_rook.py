from chess.rook import Rook
from chess.board import Board
import unittest

class RookTest(unittest.TestCase):
    def test_get_moves_rook(self):
        board = Board()
        rook = Rook("BLACK")
        board.set_piece(0, 0, rook)  #pone la pieza en el 0,0
        movimientos = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]   #todos los movimientos que deberia poder hacer
        self.assertEqual(board.get_piece(0, 0).get_moves(board, 0, 0), movimientos)


if __name__ == '__main__':
    unittest.main()