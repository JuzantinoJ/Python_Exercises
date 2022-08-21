# Question 3 (25 marks)
# This question covers materials up to seminar 4. The data structure to use is List. You can use more than ONE list. No nested list or dictionary collection is required for this question.
# This question is similar to Q2, but with Scissors-Paper-Stone played like poker game.
# (a) Implement a function getHandOfShapes(size, auto) that has an integer parameter (size) representing the number of shapes and a boolean parameter (auto) indicating if the shapes are randomly selected. Size must be at least 3. If auto is False, the function will prompt the player to indicate the shapes (Scissors-Paper-Stone) they would like to have, in sequential order and returns the selected shapes as a list.
# Duplicated shapes are fine. Examples for a hand of shapes (size 6):
#  SCISSORS, PAPER, STONE, PAPER, STONE, SCISSORS
#  PAPER, PAPER, PAPER, PAPER, PAPER, PAPER

# create getHandOfShapes function with 2 arguments (size and auto) 
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

    