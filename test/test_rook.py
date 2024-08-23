from ajedrez.rook import Rook
from ajedrez.board import Board
import unittest

class RookTest(unittest.TestCase):
    def test_get_moves_rook(self):
        board = Board()
        rook = board.get_piece(0, 0) #obtiene la pieza en el 0,0

        movimientos = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]   #todos los movimientos que deberia poder hacer

        result = rook.get_moves_rook(board, 0, 0)
        self.assertEqual(result, movimientos)


if __name__ == '__main__':
    unittest.main()

