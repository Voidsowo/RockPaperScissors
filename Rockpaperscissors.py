from random import randrange

list = ["Rock", "Paper", "Scissors"]

ai = list[randrange(0,2)]

player = False
while player == False:

    print ("Rock, Paper, Scissors ")
    player = input("Enter your move: " )

    if player == ai:
        print("Tie")
    elif player == "Rock":
        if ai == "Paper":
            print("You lose, The computer played " + ai)
        else: print("You win, The computer played " + ai)
    elif player == "Scissors":
        if ai == "Paper":
            print("You win, The computer played " + ai)
        else: print("You lose, The computer played " + ai)
    elif player.lower() == "exit":
        print("Thank you for playing")
        print()
        break
    else:
        print("That's not a valid play. Check your spelling")

    print()

    player = False
    ai = list[randrange(0,2)]
