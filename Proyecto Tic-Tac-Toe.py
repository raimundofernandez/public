# Inicializar el tablero:
x = 0
y = 0
number_X = 0
number_O = 0
win_X = False
win_O = False
player_X = True
characters = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


# Imprimir el tablero.
def print_board(characters):
    print("---------")
    print("|", characters[0], characters[1], characters[2], "|")
    print("|", characters[3], characters[4], characters[5], "|")
    print("|", characters[6], characters[7], characters[8], "|")
    print("---------")


# Leer las coordenadas.
while not win_X and not win_O and " " in characters:
    coordinates = input().split()
    if len(coordinates) != 2:
        print("You should enter numbers!")
        continue
    elif number_X - number_O > 1 or number_O - number_X > 1:
        print("Impossible")
    else:
        x, y = coordinates

    try:
        x, y = int(x), int(y)
    except ValueError:
        print("You should enter numbers!")
        continue

    if x not in range(1, 4) or y not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
    else:
        index = (x - 1) * 3 + (y - 1)
        if characters[index] == "X" or characters[index] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            if player_X:
                characters = characters[:index] + ["X"] + characters[index + 1:]
                number_X = characters.count("X")
                print_board(characters)
                player_X = False

            else:
                characters = characters[:index] + ["O"] + characters[index + 1:]
                number_O = characters.count("O")
                print_board(characters)
                player_X = True

    # Definir las combinaciones ganadoras
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]]  # diagonales

    # Comprobar si alguien ganó
    for comb in winning_combinations:
        if all(characters[i] == "X" for i in comb):
            win_X = True

        elif all(characters[i] == "O" for i in comb):
            win_O = True

# Imprimir el resultado.
if number_X - number_O > 1 or number_O - number_X > 1:
    print("Impossible")
elif win_X and not win_O:
    print("X wins")
elif win_O and not win_X:
    print("O wins")
else:
    print("Draw")
