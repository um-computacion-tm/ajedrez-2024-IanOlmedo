from pieces import Piece
from board import Board
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_moves_king(self, board, from_row, from_col):
        #Como se mueve la Torre
        pass


    def posibles_movimientos(self, from_row, from_col):
        king = self.Board.get_piece(from_row, from_col)
        if king is None:  
            return []
        else:
            return king.get_moves_king(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass