import unittest
from ajedrez.chess import Chess
from ajedrez.king import King
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
        king = King("BLACK")
        self.__chess__.__board__.set_piece(4, 4, king)

        self.__chess__.move(4, 4, 5, 3)
        moved_piece = self.__chess__.__board__.get_piece(5, 3)
        self.assertIsInstance(moved_piece, King)

        empty_position = self.__chess__.__board__.get_piece(4, 4)
        self.assertIsNone(empty_position)

        self.assertEqual(self.__chess__.turn, "WHITE")

"""    def test_end_game(self):
        # Verificamos que is_playing es True antes de llamar a end_game
        self.assertTrue(self.chess.is_playing())

        # Usamos mock para verificar el mensaje en la consola
        with patch('builtins.print') as mocked_print:
            self.chess.end_game()

            # Verificamos que playing se establece en False
            self.assertFalse(self.chess.is_playing())

            # Verificamos que el mensaje "El juego ha terminado." se imprime
            mocked_print.assert_called_once_with("El juego ha terminado.")"""

if __name__ == '__main__':
    unittest.main()



