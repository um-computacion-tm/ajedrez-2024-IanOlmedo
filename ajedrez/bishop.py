from ajedrez.piezas import Piece


class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♗"
        else:
            return "♝"

    def get_moves_bishop(self, board, from_row, from_col):
        #Como se mueve la Torre
        pass


    def posibles_movimientos(self, from_row, from_col):
        bishop = self.Board.get_piece(from_row, from_col)
        if bishop is None:  
            return []
        else:
            return bishop.get_moves_bishop(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass