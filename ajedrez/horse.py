from ajedrez.piezas import Piece


class Horse(Piece):
    white_str = "♘"
    black_str = "♞"

    def get_directions_h(self):
        return [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


    def get_moves_horse(self, board, from_row, from_col):
        return self.get_moves_kh(board, from_row, from_col, self.get_directions_h())

    def mover_a_kh(self, board, from_row, from_col, to_row, to_col):
        board.get_piece(from_row, from_col)
        if to_row and to_col in self.get_moves_horse(board, from_row, from_col):
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return board.get_piece(to_row, to_col)
        else:
            return None