from pieces import Piece
from board import Board
class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)

    def get_moves_rook(self, board, from_row, from_col):
        #Como se mueve la Torre
        pass


    def posibles_movimientos(self, from_row, from_col):
        rook = self.Board.get_piece(from_row, from_col)
        if rook is None:  
            return []
        else:
            return rook.get_moves_rook(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass
    