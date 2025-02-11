from random import randint

def game():
    moves = ["Rock","Paper", "Scissors"]

    player = moves[int(input("0 - Rock \n1 - Paper\n2 - Scissors\nYour play :"))]
    pc = moves[randint(0, 2)]

    print(f"-----PC > {pc} x {player} < You-----")
    if(player == "Rock"):
        if(pc == "Paper"):
            print("PC wins !")
        elif(pc == "Rock"):
            print("Tie !")
        else:
            print("You win !")
    elif(player == "Paper"):
        if(pc == "Scissors"):
            print("PC wins !")
        elif(pc == "Paper"):
            print("Tie !")
        else:
            print("You win !")
    else:
        if(pc == "Rock"):
            print("PC wins !")
        elif(pc == "Scissors"):
            print("Tie !")
        else:
            print("You win !")

