
import random
#Create getShape function
def getShape():
    shape = input("please select a shape:").upper()
    if shape == "SCISSORS":
        print(shape)
    elif shape == "PAPER":
        print(shape)
    elif shape == "STONE":
        print(shape)
    else:
        print("Sorry, please select from scissors, paper or stone.")

#create random shape function
def getRandomShape():
    select = "scissors,paper,stone".split(",")
    randomChoice = random.choice(select).upper()
    print( randomChoice)  

# getShape()
getRandomShape()

