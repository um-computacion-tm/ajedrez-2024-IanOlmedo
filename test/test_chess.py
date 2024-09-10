import unittest
from ajedrez.chess import Chess
from ajedrez.king import King
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class ChessTest(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

    def test_inicial_turn(self):
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_is_playing(self):
        self.assertTrue(self.__chess__.is_playing(), True)

    def test_set_turn(self):
        # Establecer el turno a "BLACK"
        self.__chess__.set_turn("BLACK")
        self.assertEqual(self.__chess__.turn, "BLACK")

        # Establecer el turno a "WHITE"
        self.__chess__.set_turn("WHITE")
        self.assertEqual(self.__chess__.turn, "WHITE")

        # Probar que un turno inválido lanza un ValueError
        with self.assertRaises(ValueError):
            self.__chess__.set_turn("INVALID_TURN")

    def test_change_turn(self):
        # Turno inicial es "WHITE", al cambiar debe ser "BLACK"
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn, "BLACK")

        # Cambiar de "BLACK" de nuevo a "WHITE"
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_move_empty_position(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition):
            self.__chess__.move(4, 4, 5, 3)  # No hay ninguna pieza en (4, 4)

    def test_move_invalid_turn(self):
        # Colocar un rey negro en el tablero en (4, 4)
        king = King("BLACK")
        self.__chess__.__board__.set_piece(4, 4, king)

        # Establecer el turno como "WHITE", pero mover una pieza "BLACK"
        self.__chess__.set_turn("WHITE")
        with self.assertRaises(InvalidTurn):
            self.__chess__.move(4, 4, 5, 3)  # No es el turno del jugador negro

    def test_movimiento_valido2(self):
        # Establecer el turno manualmente a "BLACK"
        self.__chess__.set_turn("BLACK")

        # Colocar el rey negro en la posición (4, 4) usando el tablero de Chess
        king = King("BLACK")
        # Usa el nombre correcto del atributo del tablero en Chess
        self.__chess__.__board__.set_piece(4, 4, king)

        # Realizar el movimiento válido del rey desde (4, 4) a (5, 3)
        self.__chess__.move(4, 4, 5, 3)

        # Verificar que el rey se haya movido a la nueva posición (5, 3)
        moved_piece = self.__chess__.__board__.get_piece(5, 3)
        self.assertIsInstance(moved_piece, King)

        # Verificar que la posición inicial (4, 4) esté vacía
        empty_position = self.__chess__.__board__.get_piece(4, 4)
        self.assertIsNone(empty_position)

        # Verificar que el turno haya cambiado a "WHITE"
        self.assertEqual(self.__chess__.turn, "WHITE")


if __name__ == '__main__':
    unittest.main()





"""    def test_move(self):
        # Suponiendo que (0, 0) es una coordenada válida y contiene una pieza
        self.chess.move(0, 0, 0, 1)
        piece = self.chess.__board__.get_piece(0, 1)
        self.assertIsNotNone(piece)
        self.assertEqual(self.chess.turn, "BLACK")

    def test_show_board(self):
        board_str = self.chess.show_board()
        self.assertIsInstance(board_str, str)

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")"""