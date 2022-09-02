#(ii) 
#Write a function showSeatingPlan(seatingPlan) that will display the seating plan 
# as shown in Table 4-1. 
# The parameter is a dictionary representation of the seating plan.

# from Q4(i)
def readSeatingPlan(filename):
    file = open(filename,'r')
    listofseats =[]
    for l in file.readlines():
        l = l.split()
        for items in l:
            listofseats.append(items)

    seatingPlan = {}
    for i in listofseats:
        result = i.split(',')
        seatingPlan[result[0]] = list(result[1])
    file.close()
    return seatingPlan

#create showSeatingPlan function 
def showSeatingPlan(seatingPlan):
    for k,v in seatingPlan.items():
        print(f"{k:2} {'   '.join(v)}")

    #create a list of numbers for elements
    for elem in range(1,len(v) +1 ):
        print(f"{elem:4}" , end="")

# showSeatingPlan(readSeatingPlan('Monkey_Goes_East-202209081430.txt'))

def main():
    result = readSeatingPlan('Bad_Citizen-202209081930.txt')
    showSeatingPlan(result)

main()
