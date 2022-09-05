# Question 4 (ai)
#readSeatingPlan reads the filename and store the seating plan in a dictionary
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
    
def main():
    result = readSeatingPlan('Monkey Goes East-202209081430.txt')
    print(result)
main()
