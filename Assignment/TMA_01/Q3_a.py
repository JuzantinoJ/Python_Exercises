# Question 3a

# create getHandOfShapes function with 2 arguments (size and auto) 
import random 

#create random choice for player and computer
def randChoice():
    shapes = ["scissors","paper", "stone"]
    random_list= random.choice(shapes).upper()
    return random_list

#create users number of cards
def number_of_cards():
    cards = int(input("Please input the number of cards : "))
    if cards < 3:
       print('Size must be more than 3.')
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
        print(user_card_choices)
    else:
        while card_size < size:
            usersChoice = input(f"Shape {user_size}: please select a shape: ").upper()
            if usersChoice != "SCISSORS" and usersChoice != "PAPER" and usersChoice != "STONE":
                print("Please enter correct shape")
                usersChoice  = input(f"Shape {user_size}: please select a shape: ").upper()
            card_size +=1
            user_size += 1
            user_card_choices.append(usersChoice)
        print(user_card_choices) 
   
#start game in main function
def main():
    size_of_card = number_of_cards()
    getHandOfShapes(size_of_card , True)
main()

    