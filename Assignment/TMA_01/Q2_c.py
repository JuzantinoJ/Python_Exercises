# (c) Write a new version of the Scissors-Paper-Stone game that will need a player to win 
# THREE (3) consecutive rounds to be winner.  
 
# The scope of the program is as follows: 
#  At start of the game, allows player to enter his/her name. 
#  For each round, computer will randomly pick a shape, and ask player to select 
# a shape. Make use of the functions you created in question 2(a). 
#  Your program will compare the player’s shape against the computer’s pick, 
# determine the outcome of this round: 
# o Award one point to the winner. Reset the loser’s score to 0. 
# o Do not award point if it is a tie. Reset both player and computer score to 0 
#  Repeat the round until a player reaches THREE points (i.e., wins 3 consecutive 
# rounds) 

import random , math

# players name is global variable
name = input("Enter players name: ").capitalize()

#number of rounds is global, increment after every round
numOfRounds = 1

#from Question (a)
def getRandomShape():
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    return randomChoice   

#get shape of player
def getShape():
    player = input(f"{name}, please select a shape: ").upper()
    if player == "SCISSORS" or player == "PAPER" or player == "STONE":
        return player    
    else:
        print("Sorry, please select from scissors, paper or stone.")
    return player

#Compare player and computer shape 
def play():
    player = getShape()
    computer = getRandomShape()
    global numOfRounds
    if player == computer:
        print(f"Round {numOfRounds} : {name} choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return 0
    elif player == "STONE" and computer == "PAPER":
        print(f"Round {numOfRounds} : {name} choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return -1
    elif player == "SCISSORS" and computer == "STONE":
        print(f"Round {numOfRounds} : {name} choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return -1
    elif player == "PAPER" and computer == "SCISSORS":
        print(f"Round {numOfRounds} : {name} choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return -1
    else:
        print(f"Round {numOfRounds} : {name} choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return 1




#determine winner
def winner():  
    playerPoint = 0
    computerPoint = 0
    while playerPoint < 3 and computerPoint < 3:
        result = play()
        if result == 0:
            playerPoint = 0
            computerPoint = 0
            print("Its a draw!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}") 
            print("-----" * 10)  
        elif result == 1:
            playerPoint += 1
            computerPoint = 0
            print("You won!")
            print(f"{name}: {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)   
        else: 
            result == -1
            computerPoint += 1
            playerPoint = 0
            print("You lost!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)  
    if playerPoint == 3:
       print(f"{name} is the winner after {numOfRounds} rounds!!")    
    elif computerPoint == 3:
        print(f"Computer is the winner after {numOfRounds} rounds!!")
        print("-----" * 10)
winner()