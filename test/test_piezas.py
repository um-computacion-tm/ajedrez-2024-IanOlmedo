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
            "♙": Pawn("WHITE"),
            "♟": Pawn("BLACK"),
            "♖": Rook("WHITE"),
            "♜": Rook("BLACK"),
            "♘": Horse("WHITE"),
            "♞": Horse("BLACK"),
            "♗": Bishop("WHITE"),
            "♝": Bishop("BLACK"),
            "♕": Queen("WHITE"),
            "♛": Queen("BLACK"),
            "♔": King("WHITE"),
            "♚": King("BLACK"),
        }
        self.__piece__ = Piece("WHITE")

    def test_str(self):
        for simbolo, piece in self.pieces.items():
            self.assertEqual(str(piece), simbolo)




# Reina, Torre, y Alfil en conjunto

    def test_get_moves_bloqueada(self):
        # Reina, Torre, y Alfil bloqueadas por piezas aliadas
        pieza = Queen("WHITE")
        self.__board__.set_piece(7, 3, pieza)
        self.assertEqual(pieza.get_moves_queen(self.__board__, 7, 3), [])

        pieza = Rook("WHITE")
        self.__board__.set_piece(7, 7, pieza)
        self.assertEqual(pieza.get_moves_rook(self.__board__, 7, 7), [])

        pieza = Bishop("WHITE")
        self.__board__.set_piece(7, 2, pieza)
        self.assertEqual(pieza.get_moves_bishop(self.__board__, 7, 2), [])

    def test_get_moves_bloqueada_enemigo(self):
        # Reina, Torre, y Alfil bloqueadas por piezas enemigas
        pieza = Queen("WHITE")
        self.__board__.set_piece(0, 3, pieza)
        expected_moves_queen = [(0, 2), (1, 2), (1, 3), (1, 4), (0, 4)]
        self.assertEqual(sorted(pieza.get_moves_queen(self.__board__, 0, 3)), sorted(expected_moves_queen))

        pieza = Rook("WHITE")
        self.__board__.set_piece(0, 0, pieza)
        expected_moves_rook = [(0, 1), (1, 0)]
        self.assertEqual(sorted(pieza.get_moves_rook(self.__board__, 0, 0)), sorted(expected_moves_rook))

        pieza = Bishop("WHITE")
        self.__board__.set_piece(0, 2, pieza)
        expected_moves_bishop = [(1, 1), (1, 3)]
        self.assertEqual(sorted(pieza.get_moves_bishop(self.__board__, 0, 2)), sorted(expected_moves_bishop))

    def test_moves_middle_board(self):
        # Test para movimiento en el medio del tablero para Reina, Torre y Alfil
        self.__board__.set_piece(4, 4, Queen("WHITE"))
        queen = self.__board__.get_piece(4, 4)
        expected_moves_queen = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (1, 4), 
                                (2, 4), (3, 4), (5, 4), (3, 3), (2, 2), (1, 1), (3, 5), (2, 6), 
                                (1, 7), (5, 5), (5, 3)]
        self.assertEqual(sorted(queen.get_moves_queen(self.__board__, 4, 4)), sorted(expected_moves_queen))

        self.__board__.set_piece(4, 4, Rook("WHITE"))
        rook = self.__board__.get_piece(4, 4)
        expected_moves_rook = [(3, 4), (2, 4), (1, 4), (5, 4), (4, 3), (4, 2), (4, 1), (4, 0), 
                            (4, 5), (4, 6), (4, 7)]
        self.assertEqual(sorted(rook.get_moves_rook(self.__board__, 4, 4)), sorted(expected_moves_rook))

        self.__board__.set_piece(4, 4, Bishop("WHITE"))
        bishop = self.__board__.get_piece(4, 4)
        expected_moves_bishop = [(3, 3), (2, 2), (1, 1), (5, 3), (3, 5), (2, 6), (1, 7), (5, 5)]
        self.assertEqual(sorted(bishop.get_moves_bishop(self.__board__, 4, 4)), sorted(expected_moves_bishop))




###CABALLO
    def test_get_moves_horse(self):
        # Centro del tablero, sin bloqueos (teniendo en cuenta que es blanco)
        self.__board__.set_piece(4, 4, Horse("WHITE"))
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE").get_moves_horse(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_get_moves_horse_blocked_by_allies(self):
        # Caballo bloqueado por piezas aliadas
        self.__board__.set_piece(4, 4, Horse("WHITE"))
        self.__board__.set_piece(2, 3, Queen("WHITE"))
        self.__board__.set_piece(3, 6, Rook("WHITE"))
        expected_moves = [(2, 5), (3, 2), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE").get_moves_horse(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))

    def test_get_moves_horse_can_capture(self):
        # Caballo puede capturar piezas enemigas
        self.__board__.set_piece(4, 4, Horse("WHITE"))
        self.__board__.set_piece(2, 3, Horse("BLACK"))
        self.__board__.set_piece(3, 6, Horse("BLACK"))
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6)]
        actual_moves = Horse("WHITE").get_moves_horse(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves))



##REEEEY


    def test_get_moves_king(self):
        # Test para movimientos del Rey en el centro del tablero
        self.__board__.set_piece(4, 4, King("WHITE"))
        actual_moves = King("WHITE").get_moves_king(self.__board__, 4, 4)
        expected_moves_king = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))

    def test_get_moves_king_blocked_by_allies(self):
        # Rey bloqueado por piezas aliadas
        self.__board__.set_piece(4, 4, King("WHITE"))
        self.__board__.set_piece(3, 4, Rook("WHITE"))
        self.__board__.set_piece(5, 4, Bishop("WHITE"))
        expected_moves_king = [(4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = King("WHITE").get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))

    def test_get_moves_king_can_capture(self):
        # Rey puede capturar piezas enemigas
        self.__board__.set_piece(4, 4, King("WHITE"))
        self.__board__.set_piece(3, 4, Rook("BLACK"))
        self.__board__.set_piece(5, 4, Bishop("BLACK"))
        expected_moves_king = [(3, 4), (5, 4), (4, 3), (4, 5), (3, 3), (3, 5), (5, 3), (5, 5)]
        actual_moves = King("WHITE").get_moves_king(self.__board__, 4, 4)
        self.assertEqual(sorted(actual_moves), sorted(expected_moves_king))





if __name__ == "__main__":
    unittest.main()
