

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