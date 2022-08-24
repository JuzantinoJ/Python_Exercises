# (b) Write a program to play the game of Scissors-Paper-Stone, using structured 
# programming. Your program will allow a player to play three rounds of Scissors-Paper-
# Stone against the computer. 
# The scope of the program is as follows: 
#  At start of the game, allow player to enter his/her name. 
#  For each round, computer will randomly pick a shape, and ask player to select 
# a shape. Make use of the functions you created in question 2(a). 
#  Your  program  will  compare the player’s shape against the computer’s pick, 
# determine the outcome of this round and award one point to the winner. Do not 
# award point if it is a tie.  
#  Display current score before start of next round. 
#  At the end of three rounds, display the winner of the game (if any). 
#  If  the  result  after  3  rounds  is  a  tie,  repeat  the  game  (3-rounds)  again,  until  a 
# winner can be determined. 

import random , math

# players name is global variable
name = input("Enter players name: ").capitalize()


#from Question (a)
def getRandomShape():
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    return randomChoice   


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
    numOfRounds = 1
    if player == computer:
        print(f"Round {numOfRounds} : Player choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        return 0
    elif player == "STONE" and computer == "PAPER":
        print(f"Round {numOfRounds} : Player choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        return -1
    elif player == "SCISSORS" and computer == "STONE":
        print(f"Round {numOfRounds} : Player choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        return -1
    elif player == "PAPER" and computer == "SCISSORS":
        print(f"Round {numOfRounds} : Player choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return -1
    else:
        print(f"Round {numOfRounds} : Player choosed : {player}")
        print(f"Round {numOfRounds} : Computer choosed : {computer}")
        numOfRounds += 1
        return 1




#determine winner
def winner():  
    playerPoint = 0
    computerPoint = 0
    numOfWins = 0
    while numOfWins < 3:
        result = play()
        if result == 0:
            numOfWins +=1
            print("Its a draw!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}") 
            print("-----" * 10)  
        elif result == 1:
            numOfWins +=1
            playerPoint += 1
            print("You won!")
            print(f"{name}: {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)   
        else: 
            result == -1
            numOfWins +=1
            computerPoint += 1
            print("You lost!")
            print(f"{name} : {playerPoint} || Computer : {computerPoint}")
            print("-----" * 10)
    #if its a tie, run the game again    
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