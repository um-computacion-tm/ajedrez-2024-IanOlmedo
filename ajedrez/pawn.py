from ajedrez.piezas import Piece

class Pawn(Piece):
    white_str = "♙"
    black_str = "♟"

    def __init__(self, color, piece_type):
        super().__init__(color, piece_type)

    def get_moves_pawn(self, board, from_row, from_col):
        moves = []
        direction = -1 if self.get_color() == "WHITE" else 1
        # Movimiento hacia adelante
        moves.extend(self.movimientos_pawn(board, from_row, from_col, direction)) #agrega los movimientos a la lista
        # Captura en diagonal
        moves.extend(self.capturas_diagonales(board, from_row, from_col, direction))

        return moves

    def movimientos_pawn(self, board, from_row, from_col, direction): 
        moves = []
        r, c = from_row + direction, from_col
        if 0 <= r < 8 and board.get_piece(r, c) is None:
            moves.append((r, c))

            start_row = 6 if self.get_color() == "WHITE" else 1
            if from_row == start_row:
                r_double = from_row + 2 * direction
                if board.get_piece(r_double, c) is None:
                    moves.append((r_double, c))

        return moves

    def capturas_diagonales(self, board, from_row, from_col, direction):
        moves = []
        for dc in [-1, 1]:
            r_diag, c_diag = from_row + direction, from_col + dc
            if 0 <= r_diag < 8 and 0 <= c_diag < 8:
                piece = board.get_piece(r_diag, c_diag)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append((r_diag, c_diag))
        return moves


    def get_valid_moves(self, board, from_row, from_col, tipo_pieza=None):
        return self.get_moves_pawn(board, from_row, from_col)

    def mover_a_pawn(self, board, from_row, from_col, to_row, to_col):
        return self.ejecutar_movimiento(board, from_row, from_col, to_row, to_col)