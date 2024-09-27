import unittest
from ajedrez.chess import Chess
from ajedrez.king import King
from ajedrez.pawn import Pawn
from ajedrez.rook import Rook
from unittest.mock import patch
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition


class ChessTest(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

    def test_inicial_turn(self):
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_is_playing(self):
        self.assertTrue(self.__chess__.is_playing(), True)

    def test_set_turn(self):
        self.__chess__.set_turn("BLACK")
        self.assertEqual(self.__chess__.turn, "BLACK")

        self.__chess__.set_turn("WHITE")
        self.assertEqual(self.__chess__.turn, "WHITE")

        with self.assertRaises(ValueError):
            self.__chess__.set_turn("INVALID_TURN")

    def test_change_turn(self):
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn, "BLACK")

        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_move_empty_position(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition):
            self.__chess__.move(4, 4, 5, 3)  # No hay ninguna pieza en (4, 4)

    def test_move_invalid_turn(self):
        king = King("BLACK")
        self.__chess__.__board__.set_piece(4, 4, king)

        self.__chess__.set_turn("WHITE")
        with self.assertRaises(InvalidTurn):
            self.__chess__.move(4, 4, 5, 3)  

    def test_movimiento_valido2(self):
        self.__chess__.set_turn("BLACK")
        king = King("BLACK","KING")
        self.__chess__.__board__.set_piece(4, 4, king)

        self.__chess__.move(4, 4, 5, 3)
        moved_piece = self.__chess__.__board__.get_piece(5, 3)
        self.assertIsInstance(moved_piece, King)

        empty_position = self.__chess__.__board__.get_piece(4, 4)
        self.assertIsNone(empty_position)


    def test_move_invalid_turn(self):
        # Colocar una pieza en el turno incorrecto
        self.__chess__.set_turn("BLACK")
        pawn = Pawn("WHITE", "PAWN")
        self.__chess__.__board__.set_piece(6, 4, pawn)

        # Intentar mover en el turno incorrecto debería lanzar una excepción
        with self.assertRaises(InvalidTurn):
            self.__chess__.move(6, 4, 5, 4)



    def test_king_capture_white_wins(self):
        self.__chess__.__board__.set_piece(0, 4, King("BLACK", "KING"))
        self.__chess__.__board__.set_piece(1, 4, Rook("WHITE", "ROOK"))

        self.__chess__.move(1, 4, 0, 4)

        self.assertFalse(self.__chess__.is_playing())
        self.assertEqual(self.__chess__.winner, "WHITE")

    def test_king_capture_black_wins(self):
        self.__chess__.__board__.set_piece(7, 4, King("WHITE", "KING"))
        self.__chess__.__board__.set_piece(6, 4, Rook("BLACK", "ROOK"))

        # Cambiar el turno a BLACK
        self.__chess__.set_turn("BLACK")

        self.__chess__.move(6, 4, 7, 4)

        self.assertFalse(self.__chess__.is_playing())
        self.assertEqual(self.__chess__.winner, "BLACK")

    def test_turn_changes(self):

        self.__chess__.__board__.set_piece(7, 0, Rook("WHITE", "ROOK"))
        self.__chess__.__board__.set_piece(6, 0, None)

        self.__chess__.move(7, 0, 6, 0)

        self.assertEqual(self.__chess__.turn, "BLACK")

    def test_invalid_turn(self):
        self.__chess__.__board__.set_piece(0, 0, Rook("BLACK", "ROOK"))

        with self.assertRaises(InvalidTurn):
            self.__chess__.move(0, 0, 1, 0)

    def test_empty_position(self):
        with self.assertRaises(EmptyPosition):
            self.__chess__.move(5, 5, 4, 4)

    def test_ambos_kings_estan(self):

        self.__chess__.__board__.set_piece(7, 4, King("WHITE", "KING"))
        self.__chess__.__board__.set_piece(0, 4, King("BLACK", "KING"))

        self.__chess__.view_king()
        self.assertTrue(self.__chess__.is_playing())
        self.assertIsNone(self.__chess__.winner)


if __name__ == '__main__':
    unittest.main()


