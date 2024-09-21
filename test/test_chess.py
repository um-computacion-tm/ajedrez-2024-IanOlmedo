import unittest
from ajedrez.chess import Chess
from ajedrez.king import King
from ajedrez.pawn import Pawn
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

    def test_move_valid_turn(self):
        # Colocar una pieza y moverla con turno válido
        self.__chess__.set_turn("WHITE")
        pawn = Pawn("WHITE")
        self.__chess__.__board__.set_piece(6, 4, pawn)

        self.__chess__.move(6, 4, 5, 4)  # Peón se mueve hacia adelante

        # Verificar que la pieza se movió correctamente
        moved_piece = self.__chess__.__board__.get_piece(5, 4)
        self.assertIsInstance(moved_piece, Pawn)

        # Verificar que la posición original está vacía
        empty_position = self.__chess__.__board__.get_piece(6, 4)
        self.assertIsNone(empty_position)

    def test_move_invalid_turn(self):
        # Colocar una pieza en el turno incorrecto
        self.__chess__.set_turn("BLACK")
        pawn = Pawn("WHITE")
        self.__chess__.__board__.set_piece(6, 4, pawn)

        # Intentar mover en el turno incorrecto debería lanzar una excepción
        with self.assertRaises(InvalidTurn):
            self.__chess__.move(6, 4, 5, 4)

    def test_move_empty_position(self):
        # Intentar mover desde una posición vacía debería lanzar una excepción
        with self.assertRaises(EmptyPosition):
            self.__chess__.move(4, 4, 5, 4)


    def test_both_kings_present(self):
        """Test que verifica que el juego no termine cuando ambos reyes están en el tablero."""
        # Colocar ambos reyes en el tablero
        self.__chess__.__board__.set_piece(0, 4, King("BLACK"))  # Rey negro en la posición inicial
        self.__chess__.__board__.set_piece(7, 4, King("WHITE"))  # Rey blanco en la posición inicial

        # Llamar a view_king y asegurarse de que no se termina el juego
        self.__chess__.view_king()

        # Verificar que no se ha llamado a end_game (simulado con un patch o flag)
        self.assertFalse(hasattr(self.__chess__, 'game_over'))


"""    def test_black_king_captured(self):
        # Colocar ambos reyes en el tablero
        self.__chess__.__board__.set_piece(0, 4, King("BLACK"))  # Rey negro en su posición inicial
        self.__chess__.__board__.set_piece(7, 4, King("WHITE"))  # Rey blanco en su posición inicial

        # Simular que una pieza captura al rey negro
        # Aquí se puede usar cualquier pieza que pueda "capturar" al rey
        # Por ejemplo, un peón blanco en la posición 0, 4 donde estaba el rey negro
        self.__chess__.__board__.ejecutar_move(0, 4, Pawn("WHITE"))  # Peón blanco "come" al rey negro

        # Llamar a view_king después de la captura
        self.__chess__.view_king()

        # Verificar que el ganador es el jugador blanco
        self.assertTrue(hasattr(self.__chess__, 'winner'))
        self.assertEqual(self.__chess__.winner, "WHITE")"""






if __name__ == '__main__':
    unittest.main()



"""    def test_move_and_capture_king(self):
        # Colocar un Rey y un Peón para simular la captura
        self.__chess__.set_turn("WHITE")
        king = King("BLACK")
        pawn = Pawn("WHITE")
        self.__chess__.__board__.set_piece(3, 5, king)
        self.__chess__.__board__.set_piece(4, 4, pawn)

        # Simular el movimiento del Peón para capturar al Rey
        self.__chess__.move(4, 4, 3, 5)  # Peón captura al Rey

        # Verificar que el juego ha terminado
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

        # Verificar que el Rey fue capturado y reemplazado por el Peón
        captured_piece = self.__chess__.__board__.get_piece(3, 5)
        self.assertIsInstance(captured_piece, Pawn)

        # Verificar que la posición original del Peón está vacía
        empty_position = self.__chess__.__board__.get_piece(4, 4)
        self.assertIsNone(empty_position)
"""
