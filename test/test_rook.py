import unittest
from ajedrez.rook import Rook
from ajedrez.board import Board


class RookTest(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE")
        self.__board__.set_piece(0, 0, self.__rook__) #pone la pieza blanca en el 7,7""""





    def test_get_moves_rook(self):  #no debe dar ningun movimiento porque esta encerrada por un peon y el caballo
        expected_moves = []
        result = self.__rook__.get_moves_rook(self.__board__, 7, 7)
        self.assertEqual(result, expected_moves)




    def test_get_moves_rook2(self):  #esta encerrado por 2 de distinto color
        expected_moves = [(0,1),(1,0)]
        result = self.__rook__.get_moves_rook(self.__board__, 0, 0)
        self.assertEqual(sorted(result), sorted(expected_moves))



    def test_rook_moves_middle_board(self):
        # Colocar la torre en el medio del tablero
        self.__board__.set_piece(4, 4, Rook("WHITE"))
        rook = self.__board__.get_piece(4, 4)
        expected_moves = [(3, 4), (2, 4), (1, 4),(5, 4),(4, 3), (4, 2), (4,1),(4,0), (4,5), (4,6), (4,7)]   # Movimientos hacia la izquierda y derecha
        ##Devuelve los movimientos deseadoss!

        actual_moves = rook.get_moves_rook(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves)) #sorted ordena

if __name__ == '__main__':
    unittest.main()

