
import unittest
from board import Board
from pieces.rook import Rook  
class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        #corroborar que get_size sea 8x8
        self.assertEqual(self.board.get_size(), (8,8))

    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook) # se fija si las torres estan bien ubicadas
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsNone(self.board.get_piece(4, 4))  #en el 4,4 no deberia haber nada en un comienzo

if __name__ == "__main__":
    unittest.main()