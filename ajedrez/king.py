from ajedrez.piezas import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def get_moves_king(self, board, from_row, from_col):
        directions = self.get_directions("KING")
        return self.get_moves_kh(board, from_row, from_col, directions)

        
    def mover_a_k(self, board, from_row, from_col, to_row, to_col):
        valid_moves = self.get_moves_king(board, from_row, from_col)

        if (to_row, to_col) in valid_moves:
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return self
        else:
            return None
