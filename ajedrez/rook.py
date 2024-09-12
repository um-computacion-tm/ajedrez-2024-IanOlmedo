from ajedrez.piezas import Piece


class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def get_moves_rook(self, board, from_row, from_col):
        directions = self.get_directions("ROOK")
        return self.get_pieces_moves_rqb(board, from_row, from_col, directions)



    def mover_a_r(self, board, from_row, from_col, to_row, to_col):
        valid_moves = self.get_moves_rook(board, from_row, from_col)

        if (to_row, to_col) in valid_moves:
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return self
        else:
            return None


