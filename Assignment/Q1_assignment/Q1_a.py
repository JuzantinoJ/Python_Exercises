# Question 1 (a)
# Create a sizing chart for users via their chest measurements

# create an input for chest measurement in float numeric type
chestMeasurement = float(input("Enter chest measurement (cm): "))
#create if else statement for sizes
if chestMeasurement < 80:
    print("Your T-Shirt size is 1")
elif chestMeasurement >=80 and chestMeasurement < 88:
    print("Your T-Shirt size is 2")
elif chestMeasurement >=88 and chestMeasurement < 96:
    print("Your T-Shirt size is 3")
elif chestMeasurement >=96 and chestMeasurement < 104:
    print("Your T-Shirt size is 4")
elif chestMeasurement >= 104 and chestMeasurement < 112:
    print("Your T-Shirt size is 5")
elif chestMeasurement >=112 and chestMeasurement <120:
    print("Your T-Shirt size is 6")
elif chestMeasurement >=120 and chestMeasurement <128:
     print("Your T-Shirt size is 7")
elif chestMeasurement >= 128:
    print("Your T-Shirt size is 8")


