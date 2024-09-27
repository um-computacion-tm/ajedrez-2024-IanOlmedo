import unittest
from ajedrez.board import Board
from ajedrez.king import King
from ajedrez.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__king__ = King("WHITE", "KING")

    def test_str_king(self):
        self.assertEqual(str(self.__king__), "♔")  
        


if __name__ == '__main__':
    unittest.main()
