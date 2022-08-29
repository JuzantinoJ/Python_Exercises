# create a read seating plan from file



def readSeatingPlan(filename):
    file = open(filename,'r')
    listofseats =[]
    #seperate data from file in to a list
    for l in file.readlines():
        l = l.split()
        # print(l)
        #loop through data in l and put into listofseats list
        for items in l:
            listofseats.append(items)
    # print(listofseats)

    #create key, value for seating plan
    seatingPlan = {}
    for i in listofseats:
        result = i.split(',')
        seatingPlan[result[0]] = list(result[1])
    
    print(seatingPlan)
    file.close()

readSeatingPlan('Monkey_Goes_East-202209081430.txt')