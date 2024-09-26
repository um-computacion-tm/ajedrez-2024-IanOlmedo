import unittest
from ajedrez.rook import Rook
from ajedrez.queen import Queen
from ajedrez.board import Board
from ajedrez.bishop import Bishop
from ajedrez.king import King
from ajedrez.horse import Horse
from ajedrez.pawn import Pawn
from ajedrez.piezas import Piece

class TestPiezas(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.pieces = {
            "♔": King("WHITE", "KING"),
            "♕": Queen("WHITE", "QUEEN"),
            "♖": Rook("WHITE", "ROOK"),
            "♗": Bishop("WHITE", "BISHOP"),
            "♘": Horse("WHITE", "HORSE"),
            "♙": Pawn("WHITE", "PAWN"),
            "♚": King("BLACK", "KING"),
            "♛": Queen("BLACK", "QUEEN"),
            "♜": Rook("BLACK", "ROOK"),
            "♝": Bishop("BLACK", "BISHOP"),
            "♞": Horse("BLACK", "HORSE"),
            "♟": Pawn("BLACK", "PAWN"),
        }


    def test_str(self):
        for simbolo, piece in self.pieces.items():
            self.assertEqual(str(piece), simbolo)

# Reina, Torre, y Alfil en conjunto

    def test_get_moves_bloqueada(self):
        # Reina, Torre, y Alfil bloqueadas por piezas aliadas
        pieza = Queen("WHITE", "QUEEN")
        self.__board__.set_piece(7, 3, pieza)
        self.assertEqual(pieza.get_valid_moves(self.__board__, 7, 3), [])

        pieza = Rook("WHITE", "ROOK")
        self.__board__.set_piece(7, 7, pieza)
        self.assertEqual(pieza.get_valid_moves(self.__board__, 7, 7), [])

        pieza = Bishop("WHITE", "BISHOP")
        self.__board__.set_piece(7, 2, pieza)
        self.assertEqual(pieza.get_valid_moves(self.__board__, 7, 2), [])

    def test_get_moves_bloqueada_enemigo(self):
        # Reina, Torre, y Alfil bloqueadas por piezas enemigas
        pieza = Queen("WHITE", "QUEEN")
        self.__board__.set_piece(0, 3, pieza)
        expected_moves_queen = [(0, 2), (1, 2), (1, 3), (1, 4), (0, 4)]
        self.assertEqual(sorted(pieza.get_valid_moves(self.__board__, 0, 3)), sorted(expected_moves_queen))

        pieza = Rook("WHITE", "ROOK")
        self.__board__.set_piece(0, 0, pieza)
        expected_moves_rook = [(0, 1), (1, 0)]
        self.assertEqual(sorted(pieza.get_valid_moves(self.__board__, 0, 0)), sorted(expected_moves_rook))

        pieza = Bishop("WHITE", "BISHOP")
        self.__board__.set_piece(0, 2, pieza)
        expected_moves_bishop = [(1, 1), (1, 3)]
        self.assertEqual(sorted(pieza.get_valid_moves(self.__board__, 0, 2)), sorted(expected_moves_bishop))

    def test_moves_middle_board(self):
        # Test para movimiento en el medio del tablero para Reina, Torre y Alfil
        self.__board__.set_piece(4, 4, Queen("WHITE", "QUEEN"))
        queen = self.__board__.get_piece(4, 4)
        expected_moves_queen = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (1, 4), 
                                (2, 4), (3, 4), (5, 4), (3, 3), (2, 2), (1, 1), (3, 5), (2, 6), 
                                (1, 7), (5, 5), (5, 3)]
        self.assertEqual(sorted(queen.get_valid_moves(self.__board__, 4, 4)), sorted(expected_moves_queen))

        self.__board__.set_piece(4, 4, Rook("WHITE","ROOK"))
        rook = self.__board__.get_piece(4, 4)
        expected_moves_rook = [(3, 4), (2, 4), (1, 4), (5, 4), (4, 3), (4, 2), (4, 1), (4, 0), 
                            (4, 5), (4, 6), (4, 7)]
        self.assertEqual(sorted(rook.get_valid_moves(self.__board__, 4, 4)), sorted(expected_moves_rook))

        self.__board__.set_piece(4, 4, Bishop("WHITE", "BISHOP"))
        bishop = self.__board__.get_piece(4, 4)
        expected_moves_bishop = [(3, 3), (2, 2), (1, 1), (5, 3), (3, 5), (2, 6), (1, 7), (5, 5)]
        self.assertEqual(sorted(bishop.get_valid_moves(self.__board__, 4, 4)), sorted(expected_moves_bishop))




###CABALLO
    def test_get_moves_horse(self):
        # Centro del tablero, sin bloqueos (teniendo en cuenta que es blanco)
        self.__board__.set_piece(4, 4, Horse("WHITE", "HORSE"))
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE", "HORSE").get_valid_moves(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_get_moves_horse_blocked_by_allies(self):
        # Caballo bloqueado por piezas aliadas
        self.__board__.set_piece(4, 4, Horse("WHITE", "HORSE"))
        self.__board__.set_piece(2, 3, Queen("WHITE", "QUEEN"))
        self.__board__.set_piece(3, 6, Rook("WHITE", "ROOK"))
        expected_moves = [(2, 5), (3, 2), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE", "HORSE").get_valid_moves(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_get_moves_horse_can_capture(self):
        # Caballo puede capturar piezas enemigas
        self.__board__.set_piece(4, 4, Horse("WHITE", "HORSE"))
        self.__board__.set_piece(2, 3, Horse("BLACK", "HORSE"))
        self.__board__.set_piece(3, 6, Horse("BLACK", "HORSE"))
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE", "HORSE").get_valid_moves(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))



##REEEEY


    def test_get_moves_king(self):
        # Test para movimientos del Rey en el centro del tablero
        self.__board__.set_piece(4, 4, King("WHITE", "KING"))
        actual_moves = King("WHITE", "KING").get_valid_moves(self.__board__, 4, 4)
        expected_moves_king = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))

    def test_get_moves_king_blocked_by_allies(self):
        # Rey bloqueado por piezas aliadas
        self.__board__.set_piece(4, 4, King("WHITE", "KING"))
        self.__board__.set_piece(3, 4, Rook("WHITE", "ROOK"))
        self.__board__.set_piece(5, 4, Bishop("WHITE", "BISHOP"))
        expected_moves_king = [(4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = King("WHITE", "KING").get_valid_moves(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))

    def test_get_moves_king_can_capture(self):
        # Rey puede capturar piezas enemigas
        self.__board__.set_piece(4, 4, King("WHITE", "KING"))
        self.__board__.set_piece(3, 4, Rook("BLACK", "ROOK"))
        self.__board__.set_piece(5, 4, Bishop("BLACK", "BISHOP"))
        expected_moves_king = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = King("WHITE", "KING").get_valid_moves(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))


    def test_mover_a(self):
        # Test moving a Rook
        self.__board__.set_piece(2, 3, Rook("WHITE", "ROOK"))
        self.__board__.set_piece(2, 4, Rook("BLACK", "ROOK"))
        self.__board__.get_piece(2, 3).mover_a(self.__board__, 2, 3, 2, 4)
        self.assertIsNone(self.__board__.get_piece(2, 3))
        self.assertEqual(self.__board__.get_piece(2, 4).__class__.__name__, "Rook")
        self.assertEqual(self.__board__.get_piece(2, 4).get_color(), "WHITE")

        # Test moving a Queen
        self.__board__.set_piece(3, 3, Queen("WHITE", "QUEEN"))
        self.__board__.set_piece(3, 4, Queen("BLACK","QUEEN"))
        self.__board__.get_piece(3, 3).mover_a(self.__board__, 3, 3, 3, 4)
        self.assertIsNone(self.__board__.get_piece(3, 3))
        self.assertEqual(self.__board__.get_piece(3, 4).__class__.__name__, "Queen")
        self.assertEqual(self.__board__.get_piece(3, 4).get_color(), "WHITE")


if __name__ == "__main__":
    unittest.main()
