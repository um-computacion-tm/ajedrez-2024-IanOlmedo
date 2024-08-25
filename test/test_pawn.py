import unittest
from ajedrez.pawn import Pawn
from ajedrez.board import Board

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE")

    def test_str(self):
        self.assertEqual(str(self.__pawn__), "♙")

    def test_get_moves_pawn(self):
        self.__board__.set_piece(6,3, self.__pawn__)
        pawn = self.__board__.get_piece(6,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 6, 3), [(5,3),(4,3)])
    
    def test_get_moves_pawn(self):
        self.__board__.set_piece(2,4, self.__pawn__)
        pawn = self.__board__.get_piece(2,4)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 2, 4), [(1,3),(1,5)])

    def test_un_move_pawn_(self):
        self.__board__.set_piece(3,3, self.__pawn__)
        pawn = self.__board__.get_piece(3,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 3, 3), [(2,3)])

    def test_frente_a_otro(self):
        self.__board__.set_piece(3,3, self.__pawn__)
        self.__board__.set_piece(2,3, Pawn("BLACK"))
        pawn = self.__board__.get_piece(3,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 3, 3), [])

    def test_move_a_vacia(self):
        self.__board__.set_piece(3,3, self.__pawn__)
        pawn = self.__board__.get_piece(3,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 3, 3), [(2,3)])

    def test_pawn_double_move(self):
        # Colocar un peón blanco en su posición inicial
        pawn = Pawn("WHITE")
        self.__board__.set_piece(6, 4, pawn)

        # Obtener los movimientos posibles para el peón
        actual_moves = pawn.get_moves_pawn(self.__board__, 6, 4)

        # Verificar que el peón puede moverse dos casillas hacia adelante
        expected_moves = [(5, 4), (4, 4)]
        self.assertIn((4, 4), actual_moves)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_pawn_move(self):
        self.__board__.set_piece(6, 4, Pawn("WHITE"))
        pawn = self.__board__.get_piece(6, 4)
        
        pawn.mover_a(self.__board__, 6, 4, 4, 4)# Mover el peón a la posición (4, 4)
        
        self.assertEqual(self.__board__.get_piece(4, 4), pawn) #ver si el peon esta en la 4,4
        
        self.assertIsNone(self.__board__.get_piece(6, 4)) #la casilla anterior tiene que estar en none