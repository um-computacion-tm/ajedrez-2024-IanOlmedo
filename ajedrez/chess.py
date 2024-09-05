from ajedrez.board import Board
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def set_turn(self, turn):
        if turn in ["WHITE", "BLACK"]:
            self.__turn__ = turn
        else:
            raise ValueError("Turno no válido. Debe ser 'WHITE' o 'BLACK'")



