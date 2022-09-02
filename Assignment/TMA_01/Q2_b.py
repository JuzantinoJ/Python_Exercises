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

import random

# get player name
def playerName():
    name = input("Enter player's name: ").capitalize()
    return name

#get players shape
def getShape(tries,name):
    shape = input(f"Round {tries}: {name}, please select a shape: ").upper()
    if shape == "SCISSORS":
        return shape
    elif shape == "PAPER":
        return shape
    elif shape == "STONE":
        return shape
    else:
        print("Sorry, please select from Scissors, Paper or Stone.")

#get random shape for computer
def getRandomShape(tries):
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    print(f"Round {tries}: Computer's shape is {randomChoice}")
    return randomChoice  

#compare cards to determine winner
def checkCards(player, comp):
    if player == comp:
        return 0
    elif player == "SCISSORS" and comp == "PAPER":
        return 1
    elif player == "PAPER" and comp == "STONE":
        return 1
    elif player == "STONE" and comp == "SCISSORS":
        return 1
    else:
        return -1

#start game with 3 rounds (range(1,4)). and print player and computer points
#if its a tie, play again
def play(name):
    player_point = 0
    comp_point = 0 
    for tries in range(1,4):
        user = getShape(tries,name)
        comp = getRandomShape(tries)
        cards = checkCards(user,comp)
        if cards == 0:
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
        elif cards == 1:
            player_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
        else:
            comp_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
    if player_point == comp_point:
        print("It's a tie!! Rematch...")
        play(name)
    elif player_point > comp_point:
        print("Player wins!!")
    else:
        print("Computer wins!!")

def main():
    name = playerName()
    play(name)

main()
