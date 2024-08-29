import unittest
from ajedrez.queen import Queen
from ajedrez.board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__queen__ = Queen("WHITE")


    def test_str(self):
        self.assertEqual(str(self.__queen__), "♕")



    def test_get_moves_queen(self):  #encerrado por mismo color
        expected_moves = []
        result = self.__queen__.get_moves_queen(self.__board__, 7, 3)
        self.assertEqual(result, expected_moves)



    def test_get_moves_queen2(self):  #esta encerrado por 2 de distinto color
        expected_moves = [(0,2),(1,2), (1,3),(1,4), (0,4) ]
        result = self.__queen__.get_moves_queen(self.__board__, 0, 3)
        self.assertEqual(sorted(result), sorted(expected_moves))
##Exelenteeeee



    def test_queen_moves_middle_board(self):
        # Colocar la torre en el medio del tablero
        self.__board__.set_piece(4, 4, Queen("WHITE"))
        queen = self.__board__.get_piece(4, 4)
        expected_moves = [(4,0),(4,1),(4,2),(4,3),(4,5),(4,6),(4,7), (1,4), 
                        (2,4), (3,4), (5,4),
                        (3,3), (2,2), (1,1), (3,5),(2,6),(1,7),(5,5),(5,3)]   # movimientos pra todos lados 
        

        actual_moves = queen.get_moves_queen(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))


    def test_mover_a(self):
        # mueve a la reina del 4,4 al 5,5
        self.__queen__.mover_a(self.__board__, 4, 4, 5, 5)
        
        self.assertEqual(self.__board__.get_piece(5, 5), self.__queen__) # se fija si la reina esta en la nueva casilla
        self.assertIsNone(self.__board__.get_piece(4, 4))  #ve si la casilla inicial esta vacia

if __name__ == "__main__":
    unittest.main()
