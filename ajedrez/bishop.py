from ajedrez.piezas import Piece


class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♗"
        else:
            return "♝"

    def get_moves_bishop(self, board, from_row, from_col):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:  # Se fija si esta adentro de el tablero
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))  #no hay nada que mover 
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))  # Si es una pieza del color contrario puede comer
                        break  
                    else:
                        break  # Si es una pieza aliada, no se puede avanzar más en esta línea
                else:
                    break  # Termina si no está adentro del tablero
        return moves



    def mover_a(self, board, from_row, from_col, to_row, to_col):
        board.set_piece(to_row, to_col, self)
        board.remove_piece(from_row, from_col)