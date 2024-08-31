from ajedrez.piezas import Piece

class King(Piece):
    white_str = "♔"
    black_str =  "♚"

    def get_moves_king(self, board, from_row, from_col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self.get_moves_kh(board, from_row, from_col, directions)


