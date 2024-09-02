from ajedrez.piezas import Piece

class Queen(Piece):

    white_str = "♕"
    black_str = "♛"

    def get_directions_q(self):
        return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_moves_queen(self, board, from_row, from_col):
        return self.get_pieces_moves_rqb(board, from_row, from_col, self.get_directions_q())

    def mover_a_rqb(self, board, from_row, from_col, to_row, to_col):
        board.get_piece(from_row, from_col)
        if to_row and to_col in self.get_moves_queen(board, from_row, from_col):
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return board.get_piece(to_row, to_col)
        else:
            return None