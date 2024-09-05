import unittest
from ajedrez.chess import Chess
from ajedrez.king import King

class ChessTest(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

    def test_inicial_turn(self):
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_is_playing(self):
        self.assertTrue(self.__chess__.is_playing(), True)

    def test_movimiento_valido(self):
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