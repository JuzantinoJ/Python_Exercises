
import random 


#randChoice function is to create a random list of shapes for computer and if auto is True
# if random list has more than 2 of the same shape it will loop and create a new shape
def randChoice(size):
    random_list = []
    shapes = ["scissors","paper","stone"]
    for n in range(size):
        n = random.choice(shapes).upper() 
        if random_list.count(n) < 3:
            random_list.append(n)
            while random_list.count(n) >= 3:
                random_list.pop() 
                n = random.choice(shapes).upper()
                random_list.append(n)
    return random_list

# print(randChoice(2))

#number of cards function to ask user how many cards to play
def number_of_cards():
    cards = int(input("Enter size of hand : "))
    if cards < 3:
        cards = int(input("Re-enter size of hand (must be >= 3) : "))
        return cards
    else:
        return cards

#getHandOfShapes function takes in the size from number_of_card input
# will ask use for choice of card from player
#if player choose more than 2 of the same hand, user will be prompt to re-enter a diff card
def getHandOfShapes(size,auto):
    user_card_choices = []
    if auto == False:
        for n in range(size):
            userChoice = input(f"Shape {n + 1} : please select a shape : ").upper()
            if user_card_choices.count(userChoice) < 3:
                user_card_choices.append(userChoice)
                if user_card_choices.count(userChoice) == 3:
                    print(f'Cannot have more than 2 {userChoice}')
                    user_card_choices.pop()
                    userChoice = input(f"Shape {n + 1} : please select a shape : ").upper()
                    user_card_choices.append(userChoice)
        return user_card_choices
    elif auto == True:
        for n in range(size):
           user_card_choices = randChoice(size)
        return user_card_choices

# print(getHandOfShapes(1,True))
#compare cards from player and computer. 
#Also argument takes in name input and card size
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
            print("It's a tie!! PLAYOFF...")
            play_off(name)
    elif player_point > comp_point:
        print(f"{name} is the winner!!")
    else:
        print("Computer wins! Try again")

#play_off function will commence when its a Tie. 
def play_off(name):
    size = 1
    points = 0
    player_choice = input(f"Playoff {size}: {name}, please select a shape: ").upper()
    comp_choice = randChoice(size)
    while player_choice == comp_choice[0] and points < 1:
            print(f"Playoff {size}: computer shape is : {comp_choice[0]} ")
            size += 1 
            player_choice = input(f"Playoff {size}: {name}, please select a shape: ").upper()
    if player_choice == "SCISSORS" and comp_choice[0] == "PAPER":
        print(f"Playoff {size}: computer shape is : {comp_choice[0]} ")
        print(f'{name} is the winner!!')
        points += 1

    elif player_choice == "PAPER" and comp_choice[0] == "STONE":
        print(f"Playoff {size}: computer shape is : {comp_choice[0]} ")
        print(f'{name} is the winner!!')
        points += 1
    elif player_choice == "STONE" and comp_choice[0] == "SCISSORS":
        print(f"Playoff {size}: computer shape is : {comp_choice[0]} ")
        print(f'{name} is the winner!!')
        points += 1
    else:
        print(f"Playoff {size}: computer shape is : {comp_choice[0]} ")
        print('Computer is the winner!!')
        points += 1


#main to start structured program
def main():
    size_of_card = number_of_cards()
    name = input("Enter player's name : ").capitalize()
    comp_list = randChoice(size_of_card)
    user_list = getHandOfShapes(size_of_card, True)
    print("Game starts...")
    compare_cards(user_list,comp_list,name, size_of_card)

main()