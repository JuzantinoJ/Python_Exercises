def mainMenu():
    return int(input('''
    Main Menu - FR Productions
    ======================
    1. Bad Citizen @ 2022-09-08 19:30
    2. Bad Citizen @ 2022-09-09 19:30
    3. Monkey Goes East @ 2022-09-08 14:30
    4. Monkey Goes East @ 2022-09-09 14:30
    X. Exit
    Enter selection:  '''))

def readSeatingPlan(filename):
    row_label = []
    seat_status = []
    file = open(filename,'r')
    #seperate data from file in to a list
    for line in file.readlines():
        row,seats = line.strip().split(',')
        row_label.append(row)
        seat_status.append(list(seats))
    result = dict(zip(row_label, seat_status))
    return result

#create showSeatingPlan function 
def showSeatingPlan(seatingPlan):
    for k,v in seatingPlan.items():
        print(f"{k:2} {'   '.join(v)}")

    #create a list of numbers according to the seat rows
    for elem in range(1,len(v) +1 ):
        result = str(elem).rjust(2,'0')
        print(f"  {result:2}" , end="")

def selection(select):
    while True:
        if select == 1:
            return 'Bad Citizen-202209081930.txt'
        elif select == 2:
            return 'Bad Citizen-202209091930.txt'
        elif select == 3:
            return 'Monkey Goes East-202209081430.txt'
        elif select == 4:
            return 'Monkey Goes East-202209091430.txt'
        elif select == 'x':
            break
        else:
            print('Invalid menu choice')
    
def subMenu():
    return int(input('''
    Sub-Menu
    ========
    1. Book Seats
    2. Cancel Bookings
    X. Back to Main Menu
    Enter option: 
    '''))

def showTitle(title):
        if title == 'Bad Citizen-202209081930.txt':
            print("Production : Bad Citizen")
            print("Performance datetime: 2022-09-08 19:30")
            print("Seating Plan:")
        elif title == 'Bad Citizen-202209091930.txt':
            print("Production : Bad Citizen")
            print("Performance datetime: 2022-09-09 19:30")
            print("Seating Plan:")
        elif title == 'Monkey Goes East-202209081430.txt':
            print("Production : Monkey Goes East")
            print("Performance datetime: 2022-09-08 14:30")
            print("Seating Plan:")
        elif title == 'Monkey Goes East-202209091430.txt':
            print("Production : Monkey Goes East")
            print("Performance datetime: 2022-09-09 14:30")
            print("Seating Plan:")

def main():
    select = mainMenu()
    userChoice = selection(select)
    readseat = readSeatingPlan(userChoice)
    showTitle(userChoice)
    showSeatingPlan(readseat)
    subMenu()
main()
        