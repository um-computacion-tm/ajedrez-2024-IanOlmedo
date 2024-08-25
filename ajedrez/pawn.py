from ajedrez.piezas import Piece


class Pawn(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟"

    def get_moves_pawn(self, board, from_row, from_col):
        moves = []

        #movimiento comun hacia adelante de uno en uno
        direction = -1 if self.__color__ == "WHITE" else 1
        r, c = from_row + direction, from_col  #solo aumenta la fila porque se mueve solo para adelante
        if 0 <= r < 8: #ve si esta dentro del rango de las filas
            if board.get_piece(r, c) is None:
                moves.append((r, c))  # puede moverse hacia adelante

                
                start_row = 6 if self.__color__ == "WHITE" else 1 #si el peon esya en la fila 6 o 1 puede moverse dos casillas
                if from_row == start_row:
                    r_double = from_row + 2 * direction #cantidad de movimientos base x 2
                    if board.get_piece(r_double, c) is None: #si esta vacia puede moverse
                        moves.append((r_double, c))

        # Captura en diagonal
        for dc in [-1, 1]:  # Diagonales izquierda y derecha
            r_diag, c_diag = from_row + direction, from_col + dc #dc = 1 o -1
            if 0 <= r_diag < 8 and 0 <= c_diag < 8: #se fija si el move esta dentro del tablero
                piece = board.get_piece(r_diag, c_diag)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append((r_diag, c_diag))  # Captura en diagonal

        return moves


    def mover_a(self, board, from_row, from_col, to_row, to_col):
        board.set_piece(to_row, to_col, self)
        board.remove_piece(from_row, from_col)
