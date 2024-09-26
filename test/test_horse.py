import unittest
from ajedrez.board import Board
from ajedrez.horse import Horse
from ajedrez.pawn import Pawn
from ajedrez.queen import Queen

class TestHorse(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__horse__ = Horse("WHITE", "HORSE")

    def test_mover_horse_a(self):
        self.__board__.set_piece(3,5, self.__horse__)
        reina_negra = Queen("BLACK", "QUEEN")
        self.__board__.set_piece(1,4, reina_negra)
        self.__horse__.mover_a(self.__board__, 3, 5, 1, 4)
        self.assertEqual(self.__board__.get_piece(1,4), self.__horse__)
        self.assertIsNone(self.__board__.get_piece(3,5))


if __name__ == '__main__':
    unittest.main()

