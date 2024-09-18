from ajedrez.piezas import Piece


class Horse(Piece):
    white_str = "♘"
    black_str = "♞"

    def get_moves_horse(self, board, from_row, from_col):
        directions = self.get_directions("HORSE")
        return self.get_moves_kh(board, from_row, from_col, directions)


    def mover_a(self, board, from_row, from_col, to_row, to_col):
        return self.move_piece(board, from_row, from_col, to_row, to_col, "HORSE")