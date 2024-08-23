import unittest
from ajedrez.board import Board
from ajedrez.chess import Chess

class ChessTest(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_init(self):
        self.assertIsInstance(self.chess.__board__, Board)  
        self.assertEqual(self.chess.turn, "WHITE")

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing(),True)

    def test_move(self):
        # Suponiendo que (0, 0) es una coordenada válida y contiene una pieza
        self.chess.move(0, 0, 0, 1)
        piece = self.chess.__board__.get_piece(0, 1)
        self.assertIsNotNone(piece)
        self.assertEqual(self.chess.turn, "BLACK")

    def test_show_board(self):
        board_str = self.chess.show_board()
        self.assertIsInstance(board_str, str)

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
