import unittest
from ajedrez.bishop import Bishop
from ajedrez.board import Board 
from ajedrez.pawn import Pawn

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__bishop__ = Bishop("WHITE", "BISHOP")


    def test_bishop_move_and_capture(self):
        self.__board__.set_piece(4, 6, self.__bishop__)
        pawn = Pawn("BLACK", "PAWN")
        self.__board__.set_piece(5, 5, pawn)
        
        expected_moves = [(5,5),(3,5),(2,4),(1,3),(3,7),(5,7)]
        results = sorted(self.__bishop__.get_valid_moves(self.__board__, 4, 6))
        self.assertEqual(results, sorted(expected_moves))

        self.__bishop__.ejecutar_movimiento(self.__board__, 4, 6, 5, 5)
        self.assertEqual(self.__board__.get_piece(5, 5), self.__bishop__)
        self.assertIsNone(self.__board__.get_piece(4, 6))

    def test_movimiento_bishop_invalido(self):
        self.__board__.set_piece(6, 4, self.__bishop__)
        movimiento = self.__bishop__.ejecutar_movimiento(self.__board__, 7, 2, 4, 4)

        self.assertIsNone (movimiento)

if __name__ == "__main__":
    unittest.main()
