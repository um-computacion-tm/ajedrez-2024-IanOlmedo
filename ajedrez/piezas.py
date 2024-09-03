class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):        
        return self.white_str if self.__color__ == "WHITE" else self.black_str

    def get_color(self):
        return self.__color__

    def get_pieces_moves_rqb(self, board, from_row, from_col, directions):
        moves = []
        # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
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
    
