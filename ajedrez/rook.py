from ajedrez.piezas import Piece


class Rook(Piece):
    white_str = "♖"
    black_str = "♜"


    def get_moves_rook(self, board, from_row, from_col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos en línea recta
        return self.get_pieces_moves_rqb(board, from_row, from_col, directions)



    def mover_a(self, board, from_row, from_col, to_row, to_col):
        board.set_piece(to_row, to_col, self)
        board.remove_piece(from_row, from_col)

