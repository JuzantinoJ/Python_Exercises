# Question 4 (30 marks)
# The question covers concepts in all the seminars. Employ structure programming and use of functions to make the program modular.
# FR (Fry Rice) is a popular art theatre company and is looking for a simple application to help them dynamically setup seating arrangements for their stage performances or productions. This is important to FR due to the different measures applied during the pandemic. In addition, FR is also looking for the application to allow FR admin to perform booking and cancellation of seats.
# Apply data structures to store and process information. The scope and assumptions for this question are as follow:
# (a)
#  
# 
# Each performance has its own seating plan.
# To setup a performance, FR uses a file to store the seating plan, with filename consisting of production 
# title and performance datetime. For example,
# o Production title “Bad Citizen”, performing on 18-Oct-2022 19:30 will have the
# seating plan setup in file Bad Citizen-202210181930.txt
# o Production title “Monkey Goes East”, performing on 8-Sep-2022 14:30 will have
# the seating plan setup in file Monkey Goes East-202209081430.txt
# o See Appendix A for more files for different productions’ seating plans.
# Blocked seats are marked with #, empty or available seats are marked with O, while those booked are marked with X.
# A theatre has rows of seats. The rows are labelled A, B, C, etc and seat numbers 1, 2, 3 etc.
# A seating plan for production title “Monkey Goes East”, performing on 8-Sep-2022 2:30pm, could look as follows:

# (i) Write a function readSeatingPlan(filename) where the parameter is a string representing the filename 
# that the seating plan is stored. This function reads the file and store the seating plan in a dictionary. 
# The dictionary structure after reading the file should be as follows:
# seatingPlan = { 
# 'A':['O','X','X','X','#','X','X','X','X','#','X','X','O','O'], 
# 'B':['O','O','X','X','#','X','X','X','X','#','X','X','O','O'],
# ... ...
# 'F':['#','#','X','X','#','O','X','X','X','#','X','O','#','#'], }


def readSeatingPlan(filename):
    file = open(filename,'r')
    listofseats =[]
    #seperate data from file in to a list
    for l in file.readlines():
        l = l.split()
        # print(l)
        #loop through data in l and append into listofseats list
        for items in l:
            listofseats.append(items)
    # print(listofseats)

    #create key, value for seating plan dictionary
    seatingPlan = {}
    for i in listofseats:
        result = i.split(',')
        seatingPlan[result[0]] = list(result[1])
    file.close()
    return seatingPlan

# readSeatingPlan('Monkey_Goes_East-202209081430.txt')


def main():
    result = readSeatingPlan('Monkey_Goes_East-202209081430.txt')
    print(result)

main()
