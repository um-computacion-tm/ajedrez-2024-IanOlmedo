from ajedrez.piezas import Piece


class Queen(Piece):
    white_str = "♕"
    black_str = "♛"

    def __init__(self, color, piece_type):
        super().__init__(color, piece_type)

