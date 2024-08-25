import unittest
from ajedrez.board import Board
from ajedrez.king import King
from ajedrez.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__king__ = King("WHITE")

    def test_king_moves(self):
        self.__board__.set_piece(4, 4, self.__king__)

        # sin obstaculos
        expected_moves = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_king_moves_con_obstaculos(self):
        self.__board__.set_piece(4, 4, self.__king__)

        # piezas compas
        self.__board__.set_piece(3, 4, Pawn("WHITE"))
        self.__board__.set_piece(5, 4, Pawn("WHITE"))

        # piezas enemigas
        self.__board__.set_piece(4, 3, Pawn("BLACK"))
        self.__board__.set_piece(5, 5, Pawn("BLACK"))

        expected_moves = [(3, 3), (3, 5), (4, 3), (4, 5), (5, 3), (5, 5)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_king_moves_at_edge(self):
        self.__board__.set_piece(0, 0, self.__king__)

        # en la esquina enemiga
        expected_moves = [(0, 1), (1, 0), (1, 1)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 0, 0)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_king_moves_con_pawnN(self):
        self.__board__.set_piece(4, 4, self.__king__)

        # piezas enemiga  
        self.__board__.set_piece(3, 4, Pawn("BLACK"))

        expected_moves = [(3, 4), (3, 3), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        actual_moves = self.__king__.get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_king_mover_a(self):
        self.__board__.set_piece(7, 4, self.__king__)
        # queremos moverlo al la posicion 6,4
        self.__king__.mover_a(self.__board__, 7, 4, 6, 4)
        # ve si el rey esta en la nueva casilla y si la anterior es none
        self.assertEqual(self.__board__.get_piece(6, 4), self.__king__)
        self.assertIsNone(self.__board__.get_piece(7, 4))

    def test_king_comer_hacia_atras(self):
        self.__board__.set_piece(4, 4, self.__king__)

        enemy_pawn = Pawn("BLACK")
        self.__board__.set_piece(5, 4, enemy_pawn)

        # Mover al rey para capturar la pieza enemiga
        self.__king__.mover_a(self.__board__, 4, 4, 5, 4)

        # Comprobar que el rey se ha movido y la pieza enemiga ha sido capturada
        self.assertEqual(self.__board__.get_piece(5, 4), self.__king__)
        self.assertIsNone(self.__board__.get_piece(4, 4))
        self.assertNotEqual(self.__board__.get_piece(5, 4), enemy_pawn) #assertNoEqual --> no es igual al pawn negro

if __name__ == '__main__':
    unittest.main()
