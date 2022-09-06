#Q4b(i)
#main menu takes file from FR_Productions.txt
#element in files are seperated into production list
#position list consist of keys for each file
def mainMenu():
    position = []
    production = []
    files = open('FR_Productions.txt','r')
    print("Main Menu - FR Productions")
    print("=" * 26)
    for pos, value in enumerate(files.readlines()):
        position.append(pos+1)
        production.append(value.strip().split('-'))
        title = value.split('-')
        date = title[1].split('.')
        print(f"{pos+1}. {title[0]} @ {date[0][0:4]}-{date[0][4:6]}-{date[0][6:8]} {date[0][8:10]:}:{date[0][10:12]}")
    print('X. Exit')
    choice = input('Enter Selection: ')

    #create dictionary for postion and production
    result = dict(zip(position,production))
    #using key and value position to print items in dictionary result
    while True:
        if choice == "1":
            print(f"Production : {result[1][0]}")
            print(f"Performance datetime: {result[1][1][0:4]}-{result[1][1][4:6]}-{result[1][1][6:8]} {result[1][1][8:10]}:{result[1][1][10:12]}")
            print("Seating Plan:")
            return f'{result[1][0]}-{result[1][1]}'
        elif choice == "2":
            print(f"Production : {result[2][0]}")
            print(f"Performance datetime: {result[2][1][0:4]}-{result[2][1][4:6]}-{result[2][1][6:8]} {result[2][1][8:10]}:{result[2][1][10:12]}")
            print("Seating Plan:")
            return f'{result[2][0]}-{result[2][1]}'
        elif choice == "3":
            print(f"Production : {result[3][0]}")
            print(f"Performance datetime: {result[3][1][0:4]}-{result[3][1][4:6]}-{result[3][1][6:8]} {result[3][1][8:10]}:{result[3][1][10:12]}")
            print("Seating Plan:")
            return f'{result[3][0]}-{result[3][1]}'
        elif choice == "4":
            print(f"Production : {result[4][0]}")
            print(f"Performance datetime: {result[4][1][0:4]}-{result[4][1][4:6]}-{result[4][1][6:8]} {result[4][1][8:10]}:{result[4][1][10:12]}")
            print("Seating Plan:")
            return f'{result[4][0]}-{result[4][1]}'
        elif choice == 'xX':
            break

# mainMenu()

#read seating function from Q4(a(i))
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

#showSeatingPlan function from Q4(a(ii))
def showSeatingPlan(seatingPlan):
    for k,v in seatingPlan.items():
        print(f"{k:2} {'   '.join(v)}")

    #create a list of numbers according to the seat rows
    for elem in range(1,len(v) +1 ):
        result = str(elem).rjust(2,'0')
        print(f"  {result:2}" , end="")

#subMenu function shows 3 options to choose
#selection of Book seats, Cancel Bookings or back to main menu
def subMenu():
    return int(input('''

    Sub-Menu
    ========
    1. Book Seats
    2. Cancel Bookings
    X. Back to Main Menu
    Enter option: 
    '''))

#main function to start program
def main():
    select = mainMenu()
    readseat = readSeatingPlan(select)
    showSeatingPlan(readseat)
    subMenu()
main()
        