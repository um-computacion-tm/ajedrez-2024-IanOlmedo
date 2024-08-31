from ajedrez.piezas import Piece


class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"


    def get_moves_bishop(self, board, from_row, from_col):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self.get_pieces_moves_rqb(board, from_row, from_col, directions)

