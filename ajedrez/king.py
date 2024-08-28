from ajedrez.piezas import Piece

class King(Piece):
    white_str = "♔"
    black_str =  "♚"

    def get_moves_king(self, board, from_row, from_col):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            r, c = from_row + direction[0], from_col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:  # Verifica que está dentro del tablero
                piece = board.get_piece(r, c)
                if piece is None:
                    moves.append((r, c))  # No hay nada, puede moverse
                elif piece.get_color() != self.get_color():
                    moves.append((r, c))  # Es una pieza enemiga, puede capturarla
                # No se rompe el bucle porque el rey solo puede moverse un paso en cada dirección.


        return moves


    def mover_a(self,board, from_row, from_col, to_row, to_col):
        board.set_piece(to_row, to_col, self)
        board.remove_piece(from_row, from_col)