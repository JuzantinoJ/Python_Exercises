import random
#create function to return card size
def size_of_cards():
    cards = int(input("Enter size of hand : "))
    if cards < 3:
        cards = int(input("Re-enter size of hand (must be >= 3) : "))
        return cards
    else:
        return cards


#function to enter name
def players_name():
    name = input("Enter name: ").capitalize()
    return name


#function to create random cards
def ran_cards():
    cards = ["scissors" , "paper", "stone"]
    get_random = random.choice(cards).upper()
    return get_random

#function for user choice
def user_choice(size):
    shape_size = 0
    while shape_size < size:
        shape_size + 1
        shape = input(f"Shape {shape_size} :please select a card: ").upper()
        return shape

#function to see if player want to auto generate card or manual input
def man_or_auto():
    card = input("Type Yes to auto generate cards, Type No to manually choose card : ").upper()
    if card[0] == "Y":
        return True
    else:
        return False
       


#getHand of shapes
def getHandofShapes(size,auto):
    rounds = 0 
    card_choice =[]
    while rounds < size:
        if auto == True:
            ran_card = ran_cards()
            rounds += 1
            card_choice.append(ran_card)
        elif auto == False:
            user_card = user_choice(size)
            rounds +=1
            card_choice.append(user_card)
    print(card_choice)

def main():
    size = size_of_cards()
    auto = man_or_auto()
    players_name()
    getHandofShapes(size , auto)

main()


            

        

    
