#Test para el Tablero
import unittest
from board import Board

class BoardTest(unittest.TestCase):
    def Tablero(self):
        self.board = Board()

    def test_init(self):
        #verifica que el tablero sea 8x8
        self.assertEqual(len(self.board.__positions__), 8)
        self.assertEqual(len(self.board.__positions__[0]), 8)



    def test_get_piece(self):
        #verifica que muestre las piezas y su posicion
        self.board.get_piece(0,0)
        self.board.get_piece(7,7)




if __name__ == "__main__":
    unittest.main()