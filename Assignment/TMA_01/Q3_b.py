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



#create function to check if size is at least 3 
def checkCards():
    sizeOfHand = int(input("Enter size of hand: "))
    while sizeOfHand < 3:
        sizeOfHand = int(input(f"Please re-enter size: "))
    else:
        return sizeOfHand

import random 

def getCard():
    generateCard = input(f"Do you want to auto generate cards? (Yes or No): ").upper()
    return generateCard

def getHandOfShapes(size, auto):
    shapes = ["scissors","paper", "stone"]
    userCardChoices = []
    shapeSize = 1
    cardSize = 0
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



#create a function to start game

def play():
    checkCards()
    name = input("Enter player's name: ").capitalize()
    getHandOfShapes(checkCards, getCard)
   
    print("game starts..")


play()