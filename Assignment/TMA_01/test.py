# # def main():
# #     fileName = input("What file are the numbers in? ")
# #     infile = open(fileName,'r')
# #     sum, count = 0.0, 0
# #     for line in infile:
# #         for xStr in line.split(","):
# #             sum = sum + float(xStr)
# #             count = count + 1
# #     print("\nThe average of the numbers is", sum/count)
# #     infile.close()

# someDict = {'A': ['O','X','X','X','#','X','X','X','X','#','X','X','O','O'],
# 'B': ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']}


# for value in someDict.values():
#     # print(key , "   ".join(value))
#     print(value[:1] + value[3:])
    

# # someList = ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']

# # print(f"{(len(someList))}")

# # for k, v in someDict.items():
# #     seats = (v[0] + v [1])
# #     print(k , seats)

# # def choosetochange():
# #     choice = input("Choose seat to change: ").upper()
# #     change = {choice[0]: choice[1]}
# #     return change
# # choosetochange()

# # for key in someDict.keys():
# #     print(key)

# # for value in someDict.values():
# #     print(value)

# def change(d):
#     seat = {}
#     choice = input("Choose seat to change: ").upper()
#     # change = {choice[0]: [choice[1]]}
#     key = choice[0]
#     value = int(choice[1])
#     seat[choice[0]] = int(choice[1])
#     print(type(key))
#     print(type(value))
#     print(choice)
#     for k, v in d.items():
#         print(k[0], v[value - 1])
#     # print(d)
#     # print(change)

# change(someDict)

# import random 

# #create random choice
# def randChoice(size):
#     random_list = []
#     shapes = ["scissors","paper","stone"]
#     for n in range(size):
#         n = random.choice(shapes).upper() 
#         if random_list.count(n) < 3:
#             random_list.append(n)
#             while random_list.count(n) >= 3:
#                 random_list.pop() 
#                 n = random.choice(shapes).upper()
#                 random_list.append(n)

#     return random_list

# randChoice(4)

# #create users number of cards
# def number_of_cards():
#     cards = int(input("Please input the number of cards : "))
#     if cards < 3:
#         cards = int(input("Please input more than 3 number of cards : "))
#         return cards
#     else:
#         return cards

# #ask user if he wants to auto generate cards or manually insert cards. Will return True or False
# def generateCards():
#     generate_card = input("Would you like to auto generate cards? (Yes or No) : ").upper()
#     if generate_card == "YES":
#         return True
#     else:
#         return False

# get hand of shapes of input in auto is True or False
# def getHandOfShapes(size):
#     user_card_choices = []
#     for n in range(size):
#         userChoice = input(f"Shape {n + 1} : please select a shape : ").upper()
#         if user_card_choices.count(userChoice) < 3:
#             user_card_choices.append(userChoice)
#             if user_card_choices.count(userChoice) == 3:
#                 print(f'Cannot have more than 2 {userChoice}')
#                 user_card_choices.pop()
#                 userChoice = input(f"Shape {n + 1} : please select a shape : ").upper()
#                 user_card_choices.append(userChoice)

#     return user_card_choices

# getHandOfShapes(4)


# def not_more_than_2(user_choice):




# def main():
#     size_of_card = number_of_cards()
#     getHandOfShapes(size_of_card)

# main()


# test = ["stone", "paper", "stone", "stone", 'paper',"scissors"]

# # result = test.count("stone")
# # print(result)

# def getItems():
#     things = []
#     while True:
#         items = input("please choose something: ")
#         result = things.count(items)
#         if items == "":
#             break
#         elif result < 2:
#             things.append(items)
#         else:
#             print("can't have more than 2 same input")
#             # items = input("please choose something")
#     return things
            
# getItems()

# def notMorethan2Shapes(lst):
#     result = lst/2
#     print(result)

#     # for n in lst:
#     #     if result > 2:
#     #         lst.append(n)
#     # else:
#     #     print("can't have more than 2 same input")


# notMorethan2Shapes()





#Q1
# text = 'Sep-' + 2 + '-2022'
# print(text)
#ans : runtime error

#Q2
# text = 'alibaba'
# print(text.find("aba"))
# ans : 4


#Q3
# items = {3:[1,2,3],2:[3,4,5],1:[7,8,9]}
#ans :
# keys = list(items.keys())
# print( items[keys[1]][1])

#Q4
# f = open(file.txt','w')
#ans: runtime error

#Q5
# s ='alibaba'
# s = s.replace('a','c').replace('b','a')
# print(s)
# ans : replace a wth c and b with a


# y = 1.5
# print("y is " + y)
#ans : runtime error

# aList = ['abc', 'def', 'ghi']
# length = range(len(aList))
# print(length)
#ans: 0,1,2

# s = "dcba"
# print(sorted(s))
# s = sorted(s)
# print(s)


# grade = {'A': [['Alan', 78], ['Tom', 89]], 'B': [], 'C': [ ['Jay',86]]}
# ans :grade['A'][1][1])

# grade = {'A': ['Alan', 'Tom'], 'B': [], 'C': ['Jay']}
# ans : grade['A']

# def find(x,y):
#     while x < y:
#         print(x)
#         x += 1

# find(-4,1)


#Q
# lst=[]
# def fn(n):
#     series = []
#     if n >= 5:
#         series.append(n*n)
#         n = n + 1
#     print(n,series)

# fn(5)
# ans : n is 6, lst is [25]

# temp=''
# for s in string:
#     temp = s + temp
#     print(temp)

# num = [3,2,1,0]
# print( max( num[n]*n for n in num) )

# def f(n):
#     m = float(n)
#     # n = float(input("enter: " ))
#     print(m)

# x = f(2.0)
# print(x)

# numList=[5, 2, 3, 1, 6]
# del numList[2]
# print(numList)]

# def find(s):
#     user = input('choice :').upper()
#     comp = "PAPER"
#     points = 0
#     while user == comp and points < 1:
#             user = input('choice :').upper()
#             print(user)
#             print(comp)
#             print('its a tie')
#     if user == "SCISSORS" and comp == "PAPER":
#         print('player wins') 

# find(1)




def bookSeat():
    seat_booking = []

    seats_to_book = input("Enter seats to book: ").upper()
    seats = seats_to_book.strip().split(',')
    for i in seats:
        s = i.split()
        for items in s:
           for t in items:
              seat_booking.append(t)
    print(seat_booking)


    


bookSeat()
# row_label = []
#     seat_status = []
#     file = open(filename,'r')
#     #seperate data from file in to a list
#     for line in file.readlines():
#         row,seats = line.strip().split(',')
#         row_label.append(row)
#         seat_status.append(list(seats))
#     result = dict(zip(row_label, seat_status))
#     return result