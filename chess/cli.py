from ajed import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        from_row = int(input("De la fila: "))
        from_col = int(input("De la columna: "))
        to_row = int(input("A la fila: "))
        to_col = int(input("A la columna: "))

        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Error")



if __name__ == "__main__":
    main()