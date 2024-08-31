from ajedrez.piezas import Piece


class Horse(Piece):
    white_str = "♘"
    black_str = "♞"


    def get_moves_horse(self, board, from_row, from_col):
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        return self.get_moves_kh(board, from_row, from_col, directions)
