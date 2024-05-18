from random import randint
game=["Rock", "Paper", "Scissors"]
computer=game[randint(0,2)]
player=False
while player == False:
    player=input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie! You both chose the same")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = game[randint(0,2)]