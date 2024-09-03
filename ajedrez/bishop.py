from ajedrez.piezas import Piece


class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def get_directios_b(self):
        return [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_moves_bishop(self, board, from_row, from_col):
        return self.get_pieces_moves_rqb(board, from_row, from_col, self.get_directios_b())

    def mover_a_b(self, board, from_row, from_col, to_row, to_col):
        valid_moves = self.get_moves_bishop(board, from_row, from_col)

        if (to_row, to_col) in valid_moves:
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return self
        else:
            return None