# This question covers materials up to Seminar 3. Make use of functions, selection, and repetition 
# structures.  NO  data  structures  like  sets,  lists  or  dictionary  should  be  used  for  this  question. 
# Keep the program modular by defining other functions if necessary. 
 
# Scissors-Paper-Stone (also known by other orderings of the three items, with "stone" 
# sometimes being called "rock") is a hand game originating from China, usually played between 
# two people, in which each player simultaneously forms one of three shapes with an outstretched 
# hand. These shapes are "stone" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with 
# the index finger and middle finger extended, forming a V).  
 
# The game has three outcomes: a draw, a win or a loss. A player who decides to play stone will 
# beat another player who has chosen scissors ("stone crushes scissors" or "breaks scissors") but 
# will lose to one who has played paper ("paper covers stone"); a play of paper will lose to a play 
# of  scissors  ("scissors  cuts  paper").  If  both  players  choose  the  same  shape,  the  game  is  tied 
# (draw). [extracted from Wikipedia, the free encyclopaedia] 

# (a) Implement TWO (2)  functions: 
#  getShape() that prompts, validates and returns the player’s shape selection of 
# “Scissors”, “Paper”, “Stone” in uppercase. 
#  getRandomShape()  that  returns  a  random  pick  from  “Scissors”,  “Paper”, 
# “Stone” in uppercase. 

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
    return randomChoice  


