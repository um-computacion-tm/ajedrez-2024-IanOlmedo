from piezas import Piece
from board import Board
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_moves_queen(self, board, from_row, from_col):
        #Como se mueve la Torre
        pass


    def posibles_movimientos(self, from_row, from_col):
        queen = self.Board.get_piece(from_row, from_col)
        if queen is None:  
            return []
        else:
            return queen.get_moves_queen(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass