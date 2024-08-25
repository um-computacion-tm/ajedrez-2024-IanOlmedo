from ajedrez.piezas import Piece

class King(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♔"
        else:
            return "♚"

    def get_moves_king(self, board, from_row, from_col):
        pass


    def posibles_movimientos(self, from_row, from_col):
        king = self.Board.get_piece(from_row, from_col)
        if king is None:  
            return []
        else:
            return king.get_moves_king(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass