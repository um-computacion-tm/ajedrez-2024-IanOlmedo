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
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[0][7] = Rook("BLACK") 
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[0][1] = Horse("BLACK")
        self.__positions__[0][6] = Horse("BLACK")
        self.__positions__[7][1] = Horse("WHITE")
        self.__positions__[7][6] = Horse("WHITE")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

    def __str__(self):
        board_str = "" 
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)  # si hay una pieza la imprime
                else:
                    board_str += " "  # si no hay una pieza la imprime vacia
            board_str += "\n"   
        return board_str
    
    def get_size(self):
        return len(self.__positions__)

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    

