class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):        
        return self.white_str if self.__color__ == "WHITE" else self.black_str

    def get_color(self):
        return self.__color__
    
    def get_directions(self, tipo_pieza):
        directions = {
            "BISHOP": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            "HORSE": [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)],
            "KING": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
            "QUEEN": [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
            "ROOK": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        }
        return directions.get(tipo_pieza.upper(), [])

    def get_pieces_moves_rqb(self, board, from_row, from_col, directions):
        moves = []
        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break
        return moves

    def get_moves_kh(self, board, from_row, from_col, directions):
        moves = []
        for direction in directions:
            r, c = from_row + direction[0], from_col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.get_piece(r, c)
                if piece is None:
                    moves.append((r, c))
                elif piece.get_color() != self.get_color():
                    moves.append((r, c))
        return moves
    
    
    def move_piece(self, board, from_row, from_col, to_row, to_col, tipo_pieza):
        valid_moves = self.get_valid_moves(board, from_row, from_col, tipo_pieza)
        return self.ejecutar_movimiento(board, from_row, from_col, to_row, to_col, valid_moves)

    def get_valid_moves(self, board, from_row, from_col, tipo_pieza):
        directions = self.get_directions(tipo_pieza)
        
        if tipo_pieza.upper() in ["ROOK", "BISHOP", "QUEEN"]:
            return self.get_pieces_moves_rqb(board, from_row, from_col, directions)
        else:
            return self.get_moves_kh(board, from_row, from_col, directions)
        
        
    def ejecutar_movimiento(self, board, from_row, from_col, to_row, to_col, valid_moves):
        if (to_row, to_col) in valid_moves:
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return self
        else:
            return None

