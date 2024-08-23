from ajedrez.piezas import Piece


class Horse(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♘"
        else:
            return "♞"


    def get_moves_horse(self, board, from_row, from_col):
        pass


    def posibles_movimientos(self, from_row, from_col):
        horse = self.Board.get_piece(from_row, from_col)
        if horse is None:  
            return []
        else:
            return horse.get_moves_horse(self.Board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass