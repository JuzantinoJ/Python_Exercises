# Convert temperature in fahrenheit to centigrade


from curses.ascii import isdigit

#create input stored in fahrenheit var
fahrenheit = (input("Enter your Temperature in Fahrenheit :"))

#calculate and convert fahrenheit to centigrade
if fahrenheit.isdigit():
    celcius = 5/9 * (float(fahrenheit) - 32)
    print(f"{fahrenheit} fahrenheit in centrigrade is {celcius:.2f} celcius.")
else:
     print("Please insert a number")
print("end")