

import random

#get players name
def playerName():
    name = input("Enter player's name: ").capitalize()
    return name

#get player choice
def getShape(tries,name):
    shape = input(f"Round {tries}: {name}, please select a shape: ").upper()
    if shape == "SCISSORS":
        return shape
    elif shape == "PAPER":
        return shape
    elif shape == "STONE":
        return shape
    else:
        print("Sorry, please select from scissors, paper or stone.")

#get computer choice
def getRandomShape(tries):
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    print(f"Round {tries}: Computer's shape is {randomChoice}")
    return randomChoice  

#check player and computer choices for winner
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

#play game and decides who wins the round 
def play(name):
    player_point = 0
    comp_point = 0
    tries = 1 
    while player_point < 3 and comp_point <3:
        user = getShape(tries,name)
        comp = getRandomShape(tries)
        cards = checkCards(user,comp)
        if cards == 0:
            tries += 1
            player_point = 0
            comp_point = 0
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
        elif cards == 1:
            player_point += 1
            comp_point = 0
            tries += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
        else:
            comp_point += 1
            player_point = 0
            tries += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
    if player_point == 3:
        print(f"Player is the winner after {tries} round !!")
    elif comp_point == 3:
        print(f"Computer is the winner after {tries} round !!")

#main to start game
def main():
    name = playerName()
    play(name)

main()