from ajedrez.piezas import Piece


class Rook(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

    def get_moves_rook(self, board, row, col):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

        for direction in directions:
            r, c = row, col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:  # Se fija si esta adentro de el tablero
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))  # si no hay una pieza el movimiento es valido
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))  # Si es una pieza del color contrario puede comer
                        break  
                    else:
                        break  # Si es una pieza aliada, no se puede avanzar más en esta dirección
                else:
                    break  # Termina si no está adentro del tablero

        return moves

    def posibles_movimientos(self, board, from_row, from_col):
        rook = board.get_piece(from_row, from_col)
        if rook is None:  
            return []
        else:
            return rook.get_moves_rook(board, from_row, from_col)

    def mover_a(self, from_row, from_col, to_row, to_col):
        pass
