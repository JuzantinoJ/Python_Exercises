
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
        play(name) #will start game again if its a tie
    elif player_point > comp_point:
        print("Player wins!!")
    else:
        print("Computer wins!!")

#start game
def main():
    name = playerName()
    play(name)

main()
