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
        for n in usersChoice.count(user_card_choices):
                if n > 2:
                    card_size -= 1
                else:
                    continue
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
        for n in usersChoice.count(user_card_choices):
                if n > 2:
                    print(f"Cannot have more than 2 {n}")
                    card_size -= 1
                else:
                    continue
        return user_card_choices
   

#create computer hand according to size input
def computer_hand(size):
    card_size = 0
    comp_card_choices = []
    while card_size < size:
        comp_random_list = randChoice()
        card_size += 1
        comp_card_choices.append(comp_random_list)
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
            generateCard = generateCards()
            comp = computer_hand(size_of_card)
            player = getHandOfShapes(size_of_card ,generateCard)
            compare_cards(player,comp,name, size_of_card)   
    elif player_point > comp_point:
        print(f"{name} is the winner!!")
    else:
        print("Computer wins! Try again")



#main to start structured program



def play_off(name):
    points = 0
    player_points = 0
    comp_points = 0
    round = 1
    while points < 1:
        player_choice = input(f"Playoff {round}: {name}, please select a shape: ").upper()
        comp_choice = randChoice()
        if player_choice == comp_choice:
            round += 1
            print(f"Playoff {round} Computer's shape is : {comp_choice}")
        elif player_choice == "STONE" and comp_choice == "SCISSORS":
            player_points += 1
            round += 1
            points += 1
            print(f"Playoff {round} Computer's shape is : {comp_choice}")
        elif player_choice == "SCISSORS" and comp_choice == "PAPER":
            player_points += 1
            round += 1
            points += 1
            print(f"Playoff {round} Computer's shape is : {comp_choice}")
        elif player_choice == "PAPER" and comp_choice == "STONE":
            player_points += 1
            round += 1
            points += 1
            print(f"Playoff {round} Computer's shape is : {comp_choice}")
        else:
            comp_points += 1
            round += 1
            points += 1
            print(f"Playoff {round} Computer's shape is : {comp_choice}")
    if player_points > comp_points:
        print(f"{name} wins")
    else:
        print("Computer wins")

def main():
    size_of_card = number_of_cards()
    name = input("Enter player's name : ").capitalize()
    generateCard = generateCards()
    comp_list = computer_hand(size_of_card)
    user_list = getHandOfShapes(size_of_card ,generateCard)
    print("Game starts...")
    compare_cards(user_list,comp_list,name, size_of_card)

main()
