from ajedrez.board import Board
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition
from ajedrez.king import King  

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.playing = True

    def is_playing(self):
        return self.playing
    
    def end_game(self):
        self.playing = False  
        print(f"El juego ha terminado.")

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__: 
            raise InvalidTurn()
        
        captured_piece = self.__board__.ejecutar_move(from_row, from_col, to_row, to_col)
        
        if captured_piece:
            if isinstance (captured_piece, King):
                self.end_game()
            else:
                self.change_turn()


    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def set_turn(self, turn):
        if turn in ["WHITE", "BLACK"]:
            self.__turn__ = turn
        else:
            raise ValueError("Turno no válido. Debe ser 'WHITE' o 'BLACK'")
