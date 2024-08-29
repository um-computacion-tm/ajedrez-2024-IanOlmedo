import unittest
from ajedrez.bishop import Bishop
from ajedrez.board import Board 
from ajedrez.pawn import Pawn

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__bishop__ = Bishop("WHITE")

    def test_str(self):
        self.assertEqual(str(self.__bishop__), "♗")

    def test_get_moves_bishop(self):
        self.__board__.set_piece(7,3, self.__bishop__)
        expected_moves = []

        self.assertEqual(self.__bishop__.get_moves_bishop(self.__board__, 7, 3), expected_moves)

    def test_get_moves_bishop2(self): #puede comer un peon
        self.__board__.set_piece(5,0, self.__bishop__)
        expected_moves = [(4,1),(3,2),(2,3),(1,4)]

        self.assertEqual(self.__bishop__.get_moves_bishop(self.__board__, 5, 0), expected_moves)

    def test_mover_a(self):
        self.__board__.set_piece(4,6, self.__bishop__)
        pawn = Pawn("BLACK")
        self.__board__.set_piece(5,5, pawn)
        self.__bishop__.mover_a(self.__board__, 4, 6, 5, 5)
        self.assertEqual(self.__board__.get_piece(5,5), self.__bishop__)
        self.assertIsNone(self.__board__.get_piece(4,6))