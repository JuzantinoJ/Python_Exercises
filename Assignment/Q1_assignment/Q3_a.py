# Question 3 (25 marks)
# This question covers materials up to seminar 4. The data structure to use is List. You can use more than ONE list. No nested list or dictionary collection is required for this question.
# This question is similar to Q2, but with Scissors-Paper-Stone played like poker game.
# (a) Implement a function getHandOfShapes(size, auto) that has an integer parameter (size) representing the number of shapes and a boolean parameter (auto) indicating if the shapes are randomly selected. Size must be at least 3. If auto is False, the function will prompt the player to indicate the shapes (Scissors-Paper-Stone) they would like to have, in sequential order and returns the selected shapes as a list.
# Duplicated shapes are fine. Examples for a hand of shapes (size 6):
#  SCISSORS, PAPER, STONE, PAPER, STONE, SCISSORS
#  PAPER, PAPER, PAPER, PAPER, PAPER, PAPER

# create getHandOfShapes function with 2 arguments (size and auto) 
import random 

cardSize = int(input("Please insert size: "))
generateCard = input(f"Do you want to auto generate cards? (Yes or No): ").upper()
shapes = ["scissors","paper", "stone"]
userCardChoices = []
shapeSize = 1

def getHandOfShapes(size,auto):
    cardSize = 0
    global shapeSize
    if size > 3:
        if auto == "YES":
            while cardSize < size:
                random_list= random.choice(shapes).upper()
                cardSize += 1
                shapeSize += 1
                userCardChoices.append(random_list)
            print(userCardChoices)
        elif auto == "NO":
            while cardSize < size:
                usersChoice = input(f"Shape {shapeSize}: please select a shape: ").upper()
                cardSize +=1
                shapeSize += 1
                userCardChoices.append(usersChoice)
            print(userCardChoices) 
    elif size < 3:
        print("Please choose more than 3 cards")

getHandOfShapes(cardSize,generateCard)


    