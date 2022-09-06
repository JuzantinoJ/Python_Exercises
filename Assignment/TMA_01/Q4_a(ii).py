# from Q4(i)
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

def main():
    result = readSeatingPlan('Monkey Goes East-202209081430.txt')
    showSeatingPlan(result)
main()
