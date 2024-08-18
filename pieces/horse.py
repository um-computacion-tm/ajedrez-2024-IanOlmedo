from piezas import Piece
from board import Board

class Horse(Piece):
    def __init__(self, color):
        super().__init__(color)


    def get_moves_horse(self, board, from_row, from_col):
        #Como se mueve la Torre
        pass


    def posibles_movimientos(self, from_row, from_col):
        horse = self.Board.get_piece(from_row, from_col)
        if horse is None:  
            return []
        else:
            return horse.get_moves_horse(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass