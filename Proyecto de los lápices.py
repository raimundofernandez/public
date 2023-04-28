import random

while True:
    try:
        print("How many pencils would you like to use:")
        pencils = input()
        pencils = int(pencils)
        if pencils == 0:
            print("The number of pencils should be positive.")
            continue
        elif pencils < 0:
            print("The number of pencils should be numeric.")
            continue
        else:
            break
    except ValueError:
        print("The number of pencils should be numeric.")

players = ['John', 'Jack']

current_player = 0

while True:
    print('Who will be the first (John, Jack):')
    next_player = str(input())
    if next_player == "John":
        current_player = 0
        break
    elif next_player == "Jack":
        current_player = 1
        break
    else:
        print("Choose between 'John' and 'Jack'")
        continue

while pencils != 0:
    while True:
        try:
            print(str("|") * int(pencils))
            print(players[current_player] + "'s turn:")
            if players[current_player] == "John":
               resta = int(input())
            else:
               if pencils % 4 == 5:
                   resta = random.choice([1, 2, 3])
               elif pencils % 4 == 0:
                   resta = 3
               elif pencils % 4 == 3:
                   resta = 2
               else:
                   resta = 1
               print(resta)
            if resta == 1 or resta == 2 or resta == 3:
                if resta > pencils:
                    print("Too many pencils were taken")
                    continue
                else:
                    pencils -= resta
                    current_player = (current_player + 1) % 2
                    if pencils == 0:
                        print(players[current_player], "won!")
                        break
                    else:
                        continue
            else:
                print("Possible values: '1', '2' or '3'")
                continue
        except ValueError:
            print("Possible values: '1', '2' or '3'")
