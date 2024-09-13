from ajedrez.piezas import Piece


class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def get_moves_rook(self, board, from_row, from_col):
        directions = self.get_directions("ROOK")
        return self.get_pieces_moves_rqb(board, from_row, from_col, directions)



    def mover_a(self, board, from_row, from_col, to_row, to_col):
        return self.move_piece(board, from_row, from_col, to_row, to_col, "ROOK")

