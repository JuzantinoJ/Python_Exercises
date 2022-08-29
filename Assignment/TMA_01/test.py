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

someDict = {'A': ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']}

for key,value in someDict.items():
    print(key , "   ".join(value))

someList = ['O','X','X','X','#','X','X','X','X','#','X','X','O','O']

print(f"{(len(someList))}")
