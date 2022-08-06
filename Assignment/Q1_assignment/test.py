import random

# def getRandomShape():
#     shape1 = "scissors"
#     shape2 = "paper"
#     shape3 = "stone"
#     allShapes = shape1 , shape2 ,shape3
#     randomShapes = random.choice(allShapes).upper()
#     if randomShapes == "SCISSORS":
#         print(f"Computer shape is : SCISSORS")
#     elif randomShapes == "PAPER":
#         print(f"Computer shape is : PAPER")
#     elif randomShapes == "STONE":
        # print(f"Computer shape is : STONE")




# player = "SCISSORS"
# shape1 = "scissors"
# shape2 = "paper"
# shape3 = "stone"
# allShapes = shape1 , shape2 ,shape3
# computer = random.choice(allShapes).upper()
# if player == "SCISSORS" and computer == "SCISSORS":
#     print("Its a draw")
# elif player == "SCISSORS" and computer == "PAPER":
#     print("PLAYER WINS")
# elif player == "SCISSORS" and computer == "STONE":
#     print("Computer wins!")

# import random

# def getRandomShape():
#     shape1 = "scissors"
#     shape2 = "paper"
#     shape3 = "stone"
#     allShapes = shape1 , shape2 ,shape3
#     return f"Computer shape is: {random.choice(allShapes).upper()}"

# computer = getRandomShape
# print(computer())

import random , math
name = input("Enter players name: ").capitalize()


def getRandomShape():
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    return randomChoice   
# getRandomShape()

def getShape():
    player = input(f"{name}, please select a shape: ").upper()
    if player == "SCISSORS" or player == "PAPER" or player == "STONE":
        print(f"Player choosed : {player}")     
    else:
        print("Sorry, please select from scissors, paper or stone.")
    return player

def play():
    player = getShape()
    computer = getRandomShape()
    if player == computer:
        print(f"Computer choosed : {computer}")
        return (0)
    elif player == "STONE" and computer == "PAPER":
        print(f"Computer choosed : {computer}")
        return -1
    elif player == "SCISSORS" and computer == "STONE":
        print(f"Computer choosed : {computer}")
        return -1
    elif player == "PAPER" and computer == "SCISSORS":
        print(f"Computer choosed : {computer}")
        return -1
    else:
        print(f"Computer choosed : {computer}")
        return 1


def winner():  
    playerPoint = 0
    computerPoint = 0
    numOfRounds = 0
    while numOfRounds < 3:
        result = play()
        if result == 0:
            numOfRounds +=1
            print("Its a draw!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}") 
            print("-----" * 10)  
        elif result == 1:
            numOfRounds +=1
            playerPoint += 1
            print("You won!")
            print(f"{name}: {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)   
        else: 
            result == -1
            numOfRounds +=1
            computerPoint += 1
            print("You lost!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)
        
    if playerPoint == computerPoint:
        print(f"Its a tie!! Rematch...")
        print("-----" * 10)
        winner()     
    elif playerPoint > computerPoint:
        print(f"{name} is the winner!!")
        print("-----" * 10)
    else:
        print(f"Computer is the winner!!")
        print("-----" * 10)
winner()

