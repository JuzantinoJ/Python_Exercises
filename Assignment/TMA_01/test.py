# def main():
#     fileName = input("What file are the numbers in? ")
#     infile = open(fileName,'r')
#     sum, count = 0.0, 0
#     for line in infile:
#         for xStr in line.split(","):
#             sum = sum + float(xStr)
#             count = count + 1
#     print("\nThe average of the numbers is", sum/count)
#     infile.close()

someDict = {'A': ['O','X','X','X','#','X','X','X','X','#','X','X','O','O'],
'B': ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']}


for value in someDict.values():
    # print(key , "   ".join(value))
    print(value[:1] + value[3:])
    

# someList = ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']

# print(f"{(len(someList))}")

# for k, v in someDict.items():
#     seats = (v[0] + v [1])
#     print(k , seats)

# def choosetochange():
#     choice = input("Choose seat to change: ").upper()
#     change = {choice[0]: choice[1]}
#     return change
# choosetochange()

# for key in someDict.keys():
#     print(key)

# for value in someDict.values():
#     print(value)

def change(d):
    seat = {}
    choice = input("Choose seat to change: ").upper()
    # change = {choice[0]: [choice[1]]}
    key = choice[0]
    value = int(choice[1])
    seat[choice[0]] = int(choice[1])
    print(type(key))
    print(type(value))
    print(choice)
    for k, v in d.items():
        print(k[0], v[value - 1])
    # print(d)
    # print(change)

change(someDict)