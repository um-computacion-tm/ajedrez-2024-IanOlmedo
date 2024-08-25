import unittest
from ajedrez.horse import Horse
from ajedrez.board import Board
from ajedrez.pawn import Pawn

class TestHorse(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__horse__ = Horse("WHITE")

    def test_str(self):
        self.assertEqual(str(self.__horse__), "♘") 

    def test_get_moves_horse(self): #posicion inicial de blancas
        self.__board__.set_piece(7, 6, self.__horse__)
        expected_moves = [(5,5), (5,7)]
        self.assertEqual(self.__horse__.get_moves_horse(self.__board__, 7, 6), expected_moves)

    def test_caballo_en_el_medio(self):
        self.__board__.set_piece(3,6, self.__horse__)
        expected_moves = [(1,5),(1,7), (2,4),(4,4), (5,5), (5,7)]
        self.assertEqual(sorted(self.__horse__.get_moves_horse(self.__board__, 3, 6)), sorted(expected_moves))

    def test_caballo_mover_a(self):
        self.__board__.set_piece(3,6, self.__horse__)
        pawn = Pawn("BLACK")
        self.__board__.set_piece(2,4, pawn)
        self.__horse__.mover_a(self.__board__, 3, 6, 2, 4)
        self.assertEqual(self.__board__.get_piece(2,4), self.__horse__)
        self.assertEqual(self.__board__.get_piece(3,6), None)
