#scissors paper stone
#for 2b


import random

def playerName():
    name = input("Enter player's name: ").capitalize()
    return name

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


def getRandomShape(tries):
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    print(f"Round {tries}: Computer's shape is {randomChoice}")
    return randomChoice  

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




# def winner(card):
#     if card == 0:
#         return 0
#     elif card == 1:
#         return 1
#     else:
#         return 0


# def points(name,win):
#     player_point = 0
#     comp_point = 0
#     if win == 0:
#         print(f"<< {name} {player_point} : Computer {comp_point} >>")
#     elif win == 1:
#         player_point += 1
#         print(f"<< {name} {player_point} : Computer {comp_point} >>")
#     else:
#         comp_point += 1
#         print(f"<< {name} {player_point} : Computer {comp_point} >>")






# def main():
#     name = playerName()
#     for tries in range(1,4):
#         player = getShape(tries,name)
#         comp = getRandomShape(tries)
#         card = checkCards(player,comp)
#         win = winner(card)
#         points(name,win)


# main()




# def winner(player,comp):
#     if player == comp:
#         return 0
#     elif player == "SCISSORS" and comp == "PAPER":
#         return 1
#     elif player == "PAPER" and comp == "STONE":
#         return 1
#     elif player == "STONE" and comp == "SCISSORS":
#         return 1
#     else:
#         return -1


# def play():
#     name = input("Enter player's name: ").capitalize()
#     tries = 1
#     player_point = 0
#     comp_point = 0
#     shape = input(f"Round {tries}: {name}, please select a shape: ").upper()
#     player = getShape(shape)
#     comp = getRandomShape()
#     while tries <= 3:
#         win = winner(player,comp)
#         if win == 0:
#             print(f"Round {tries}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#         elif win == 1:
#             player_point += 1
#             print(f"Round {tries}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#         elif win == -1:
#             comp_point += 1
#             print(f"Round {tries}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#     if player_point 







# def compareShape():
#     name = input("Enter player's name: ").capitalize()
#     player_point = 0
#     comp_point = 0
#     round = 0
#     while round < 3 :
#         shape = input(f"Round {round + 1}: {name}, please select a shape: ").upper()
#         player = getShape(shape)
#         comp = getRandomShape()
#         if player == comp:
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round+= 1
#         elif player == "SCISSORS" and comp == "PAPER":
#             player_point += 1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round += 1
#         elif player == "STONE" and comp == "SCISSORS":
#             player_point += 1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round += 1
#         elif player == "PAPER" and comp == "STONE":
#             player_point += 1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round += 1
#         elif player == "STONE" and comp == "PAPER":
#             comp_point +=1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round += 1
#         elif player == "PAPER" and comp == "SCISSORS":
#             round += 1
#             comp_point +=1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#         elif player == "SCISSORS" and comp == "STONE":
#             comp_point +=1
#             print(f"Round {round + 1}: Computer's shape is {comp}")
#             print(f"<< {name} {player_point} : Computer {comp_point}")
#             round += 1
#     if player_point == comp_point:
#         print("It's a tie!! Rematch")
#         compareShape()
#     elif player_point > comp_point:
#         print("Player is the winner!!")
#     else:
#         print("Computer is the winner!!")
    

# def main():
#     compareShape()

# main()