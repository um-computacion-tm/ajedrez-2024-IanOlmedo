import unittest
from ajedrez.pawn import Pawn
from ajedrez.board import Board

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE")


    def test_get_moves_pawn(self):
        self.__board__.set_piece(6,3, self.__pawn__)
        pawn = self.__board__.get_piece(6,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 6, 3), [(5,3),(4,3)])
    
    def test_get_moves_pawn2(self):
        self.__board__.set_piece(2,4, self.__pawn__)
        pawn = self.__board__.get_piece(2,4)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 2, 4), [(1,3),(1,5)])  #NO puede comer en vertical


    def test_frente_a_otro(self):
        self.__board__.set_piece(3,3, self.__pawn__)
        self.__board__.set_piece(2,3, Pawn("BLACK"))
        pawn = self.__board__.get_piece(3,3)

        self.assertEqual(pawn.get_moves_pawn(self.__board__, 3, 3), [])


    def test_pawn_mover_a(self):
        self.__board__.set_piece(6, 4, self.__pawn__)
        pawn = self.__board__.get_piece(6, 4)
        
        self.__pawn__.mover_a_pawn(self.__board__, 6, 4, 4, 4)# Mover el peón a la posición (4, 4)
        
        self.assertEqual(self.__board__.get_piece(4, 4), pawn) #ver si el peon esta en la 4,4
        
        self.assertIsNone(self.__board__.get_piece(6, 4)) #la casilla anterior tiene que estar en none

    def test_movimiento_pawn_invalido(self):
        self.__board__.set_piece(6, 4, self.__pawn__)
        movimiento = self.__pawn__.mover_a_pawn(self.__board__, 6, 4, 7, 4)

        self.assertIsNone (movimiento)