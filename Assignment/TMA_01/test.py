# #rewrite Qns3a
import random 

def randChoice():
    shapes = ["scissors","paper", "stone"]
    random_list= random.choice(shapes).upper()
    return random_list


def number_of_cards():
    cards = int(input("Please input the number of cards : "))
    if cards < 3:
        cards = int(input("Please input more than 3 number of cards : "))
        return cards
    else:
        return cards

def generateCards():
    generate_card = input("Would you like to auto generate cards? (Yes or No) : ").upper()
    if generate_card == "YES":
        return True
    else:
        return False


size_of_card = number_of_cards()
generateCard = generateCards()


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
        print(user_card_choices)
    else:
        while card_size < size:
            usersChoice = input(f"Shape {user_size}: please select a shape: ").upper()
            card_size +=1
            user_size += 1
            user_card_choices.append(usersChoice)
        print(user_card_choices) 
   

getHandOfShapes(size_of_card ,generateCard)