import unittest
from ajedrez.queen import Queen
from ajedrez.board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__queen__ = Queen("WHITE")

    def test_mover_a(self):
        self.__queen__.mover_a(self.__board__, 4, 4, 5, 5)
        self.assertEqual(self.__board__.get_piece(5, 5), self.__queen__)
        self.assertIsNone(self.__board__.get_piece(4, 4))

if __name__ == "__main__":
    unittest.main()

