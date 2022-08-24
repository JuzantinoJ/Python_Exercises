# (b)
# A sample run of this function print( getHandOfShapes(4, False) ) is as follows:
# Output from
# ['STONE', 'STONE', 'SCISSORS', 'PAPER'] print( getHandOfShapes(4, True) )
# where the 4 shapes are randomly selected
# (5 marks)
# Employ structured programming to develop a new game with rules as follows:
#  At start of the game, prompt for the size of hand.
#  Size must be at least 3. If not, ask user to re-enter the size.
#  After capturing the player’s name, proceed to create the player’s hand of shapes.
# Make use of the getHandOfShapes() function in Q3(a).
#  Your program will also setup computer’s hand of shapes, according to the size
# entered.
#  Next is to compare the computer and players’ hand of shapes, one-by-one, and
# award one point to the winner. Do not award point if it is a tie.
#  After comparing the hand of shapes, display the winner of the game (if any).
#  If the result is a tie, repeat the game with new hand of shapes, until a winner can
# be determined.

import random 

def randChoice():
    shapes = ["scissors","paper", "stone"]
    random_list= random.choice(shapes).upper()
    return random_list


def number_of_cards():
    cards = int(input("Enter size of hand : "))
    if cards < 3:
        cards = int(input("Re-enter size of hand (must be >= 3) : "))
        return cards
    else:
        return cards

def generateCards():
    generate_card = input("Would you like to auto generate cards? (Yes or No) : ").upper()
    if generate_card == "YES":
        return True
    else:
        return False


def getHandOfShapes(size,auto):
    card_size = 0
    user_size = 1
    user_card_choices = []
    if auto == True:
        while card_size < size:
            random_list= randChoice()
            card_size += 1
            user_size += 1
            user_card_choices.append(random_list)
        return user_card_choices
    else:
        while card_size < size:
            usersChoice = input(f"Shape {user_size}: please select a shape: ").upper()
            card_size +=1
            user_size += 1
            user_card_choices.append(usersChoice)
        return user_card_choices
   


def computer_hand(size):
    card_size = 0
    comp_card_choices = []
    while card_size < size:
        comp_random_list = randChoice()
        card_size += 1
        comp_card_choices.append(comp_random_list)
    return comp_card_choices

size_of_card = number_of_cards()
generateCard = generateCards()
comp_list = computer_hand(size_of_card)
user_list = getHandOfShapes(size_of_card ,generateCard)


def compare_cards(player, comp):
    name = input("Enter player's name : ").capitalize()
    round = 0
    player_point = 0
    comp_point = 0
    print("Game starts...")
    for index in range(size_of_card):
        if player[index] == comp[index]:
            round += 1
            print(f"Round {round} : {name} {player[index]} : Computer {comp[index]}")
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
            input("Press <Enter> to proceed.")
        elif player[index] == "STONE" and comp[index] == "SCISSORS":
            round += 1
            print(f"Round {round} : {name} {player[index]} : Computer {comp[index]}")
            player_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
            input("Press <Enter> to proceed.")
        elif player[index] == "SCISSORS" and comp[index] == "PAPER":
            round += 1
            print(f"Round {round} : {name} {player[index]} : Computer {comp[index]}")
            player_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
            input("Press <Enter> to proceed.")
        elif player[index] == "PAPER" and comp[index] == "STONE":
            round += 1
            print(f"Round {round} : {name} {player[index]} : Computer {comp[index]}")
            player_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
            input("Press <Enter> to proceed.")
        else:
            round += 1
            print(f"Round {round} : {name} {player[index]} : Computer {comp[index]}")
            comp_point += 1
            print(f"<< {name} {player_point} : Computer {comp_point} >>")
            input("Press <Enter> to proceed.")
    if player_point == comp_point:
        print("It's a tie!! Rematch")
        compare_cards(user_list,comp_list)
    elif player_point > comp_point:
        print("Player wins!")
    else:
        print("Computer wins! Try again")


compare_cards(user_list,comp_list)