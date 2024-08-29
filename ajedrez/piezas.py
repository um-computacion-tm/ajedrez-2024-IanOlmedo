

class Piece():
    def __init__(self, color):
        self.__color__ = color
    
    def get_pieces_moves_rqb(self, board, from_row, from_col, directions):
            moves = []
            for direction in directions:
                r, c = from_row, from_col
                while True:
                    r += direction[0]
                    c += direction[1]
                    if 0 <= r < 8 and 0 <= c < 8:  # Se fija si está dentro del tablero
                        piece = board.get_piece(r, c)
                        if piece is None:
                            moves.append((r, c))  # Si no hay nada, añade la posición a movimientos posibles
                        elif piece.get_color() != self.get_color():
                            moves.append((r, c))  # Si es una pieza enemiga, añade la posición y termina
                            break
                        else:
                            break  # Si es una pieza aliada, termina
                    else:
                        break  # Si no está dentro del tablero, termina
            return moves



    def __str__(self):        
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def get_color(self):
        return self.__color__



