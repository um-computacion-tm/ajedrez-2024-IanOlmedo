from ajedrez.piezas import Piece

class Queen(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♕"
        else:
            return "♛"

    def get_moves_queen(self, board, from_row, from_col):
        move = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] #arriba, abajo, izquierda, derecha, arriba-izquierda, arriba-derecha, abajo-izquierda, abajo-derecha
        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:  # Se fija si esta adentro de el tablero
                    piece = board.get_piece(r, c)
                    if piece is None:
                        move.append((r, c))  #no hay nada que mover 
                    elif piece.get_color() != self.get_color():
                        move.append((r, c))  # Si es una pieza del color contrario puede comer
                        break  
                    else:
                        break  # Si es una pieza aliada, no se puede avanzar más en esta línea
                else:
                    break  # Termina si no está adentro del tablero
        return move


    def posibles_movimientos(self, from_row, from_col):
        queen = self.board.get_piece(from_row, from_col)
        if queen is None:  
            return []
        else:
            return queen.get_moves_queen(self.board, from_row, from_col)


    def mover_a(self, from_row, from_col, to_row, to_col):
        pass