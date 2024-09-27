from ajedrez.rook import Rook   
from ajedrez.horse import Horse
from ajedrez.bishop import Bishop
from ajedrez.queen import Queen
from ajedrez.king import King
from ajedrez.pawn import Pawn


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        # Coloca las piezas en sus posiciones iniciales
        self.__positions__[0][0] = Rook("BLACK","ROOK")
        self.__positions__[7][7] = Rook("WHITE", "ROOK")
        self.__positions__[0][7] = Rook("BLACK","ROOK") 
        self.__positions__[7][0] = Rook("WHITE", "ROOK")
        self.__positions__[0][1] = Horse("BLACK", "HORSE")
        self.__positions__[0][6] = Horse("BLACK","HORSE")
        self.__positions__[7][1] = Horse("WHITE","HORSE")
        self.__positions__[7][6] = Horse("WHITE", "HORSE")
        self.__positions__[0][2] = Bishop("BLACK", "BISHOP")
        self.__positions__[0][5] = Bishop("BLACK","BISHOP")
        self.__positions__[7][2] = Bishop("WHITE","BISHOP")
        self.__positions__[7][5] = Bishop("WHITE", "BISHOP")
        self.__positions__[0][3] = Queen("BLACK", "QUEEN")
        self.__positions__[7][3] = Queen("WHITE", "QUEEN")
        self.__positions__[0][4] = King("BLACK", "KING")
        self.__positions__[7][4] = King("WHITE", "KING")
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK", "PAWN")
            self.__positions__[6][i] = Pawn("WHITE", "PAWN")

    def __str__(self):
        board_str = "  0 1 2 3 4 5 6 7\n"  # columna inicio
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " "  # fila final
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " " 
                else:
                    board_str += ". "  # (donde no hay piexza pongo un punto)
            board_str += str(i) + "\n"  # fila final
        board_str += "  0 1 2 3 4 5 6 7\n"  # Columnas final
        return board_str
    
    def get_size(self):
        return len(self.__positions__)

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece): 
        self.__positions__[row][col] = piece

    def remove_piece(self, row, col):
        self.__positions__[row][col] = None



    def ejecutar_move(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)

        if piece is None:
            raise ValueError("No hay ninguna pieza en la posición de origen")
        
        tipo_pieza = piece.__class__.__name__.upper() ##-->>que pieza se esta queriendo mover


        if isinstance(piece, Pawn):  ##--->porque el peon tiene metodos especificos
            moved_piece = piece.mover_a_pawn(self, from_row, from_col, to_row, to_col)
        else:
            moved_piece = piece.move_piece(self, from_row, from_col, to_row, to_col)

        if moved_piece is None:
            raise ValueError(f"Movimiento no válido para la pieza {tipo_pieza}")
        
        return moved_piece




