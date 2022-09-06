# 3(b)
import random 

#create random choice for player and computer
def randChoice():
    shapes = ["scissors","paper", "stone"]
    random_list= random.choice(shapes).upper()
    return random_list

#create users number of cards size
def number_of_cards():
    cards = int(input("Enter size of hand : "))
    while cards < 3:
        cards = int(input("Re-enter size of hand (must be >= 3) : "))
        return cards
    else:
        return cards

# get hand of shapes of input in auto is True or False
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
            if usersChoice != "SCISSORS" and usersChoice != "PAPER" and usersChoice != "STONE":
                print("Please enter correct shape")
                usersChoice  = input(f"Shape {user_size}: please select a shape: ").upper()
            card_size +=1
            user_size += 1
            user_card_choices.append(usersChoice)
        return user_card_choices
   

#create computer hand according to size input
def computer_hand(size):
    comp_card_choices = []
    for n in range(size):
        n = randChoice()
        comp_card_choices.append(n)
    return comp_card_choices

#compare cards from player and computer. Also argument takes in name input and card size
def compare_cards(player, comp, name, size_of_card):
    round = 0
    player_point = 0
    comp_point = 0
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
        comp = computer_hand(size_of_card)
        player = getHandOfShapes(size_of_card , False)
        compare_cards(player,comp,name, size_of_card)   
    elif player_point > comp_point:
        print(f"{name} is the winner!!")
    else:
        print("Computer wins! Try again")

#main to start structured program
def main():
    size_of_card = number_of_cards()
    name = input("Enter player's name : ").capitalize()
    comp_list = computer_hand(size_of_card)
    user_list = getHandOfShapes(size_of_card ,False)
    print("Game starts...")
    compare_cards(user_list,comp_list,name, size_of_card)
main()