from ajedrez.chess import Chess
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition



def main():
    print("")
    print("¡Vamos a jugar al ajedrez!")
    print("")
    chess = Chess()
    while chess.is_playing():  
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("Turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        
        chess.move(from_row, from_col, to_row, to_col)
        

        rendirse(chess)
        
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("Error:", e)

def rendirse(chess):
    respuesta = input("Jugador " + chess.turn + ", ¿Deseas rendirte? (s/n): ").lower()
    if respuesta == "s":
        print(f"El jugador {chess.turn} se ha rendido. Fin del juego.")
        chess.end_game() 
        return

if __name__ == '__main__':
    main()
