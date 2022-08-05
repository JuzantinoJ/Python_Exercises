#Question 1 (b)
# Create a program to find users size via Height, Chest and Waist measurement.
# If all sizes fit within range, indicate the best fit for user

#create variable for 3 inputs - Height ,Chest and Weight

height = float(input("Enter height measurement (cm):"))
chest = float(input("Enter chest measurement (cm):"))
waist = float(input("Enter waist measurement (cm):"))


if height < 155:
    if chest < 80 and waist < 70:
        print("You are size 1 (best fit)")
    elif chest > 80 and waist > 70:
        print("You are a size 2 regular fit")
elif height > 155:
    if chest < 80 and waist < 70:
        print("You are a size 2 (relaxed fit)")

if height >= 155 and height < 160:
    if (chest >= 80 and chest < 88) and (waist >= 70 and waist < 76):
        print("You are a size 2 (best fit)")
    elif chest > 88 and waist > 76:
        print("You are a size 3 (regular fit)")
elif height > 160:
    if chest < 88 and waist < 76:
        print("You are a size 3 (relaxed fit)")
    
if height >= 160 and height < 165:
    if(chest >= 88 and chest < 96) and (waist >= 76 and waist < 84):
        print("You are size 3 (best fit)")
    elif chest > 96 and waist > 84:
        print("You are a size 4 (regular fit)")
elif height > 165:
    if chest < 96 and waist < 84:
        print("You are a size 4 (relaxed fit)")

if height >=165 and height < 170:
    if(chest >= 96 and chest < 104) and (waist >= 84 and waist < 92):
        print("You are a size 4 (best fit)")
    elif chest > 104 and waist > 92:
        print("You are a size 5 (regular fit")
elif height > 170:
    if chest < 104 and waist < 92:
        print("You are a size 5 (relaxed fit)")

if height >=170 and height < 175:
    if(chest >= 104 and chest < 112) and (waist >= 92 and waist < 100):
        print("You are a size 5 (best fit)")
    elif chest > 112 and waist > 100:
        print("You are a size 6 (regular fit)")
elif height > 175:
    if chest < 112 and waist < 100:
        print("You are a size 6 (relaxed fit)")

if height >=175 and height < 180:
    if(chest >= 112 and chest < 120) and (waist >=100 and chest <108):
        print("You are a size 6 (best fit)")
    elif chest > 120 and waist > 108:
        print("You are a size 7 (regular fit)")
elif height > 180:
    if chest < 120 and waist <108:
        print("You are a size 7 (relaxed fit)")

if height >= 180 and height < 185:
    if(chest >= 120 and chest < 128) and (waist >=108 and waist < 116):
        print("You are a size 7 (best fit)")

#size 8
if height >= 185:
    if chest >= 128 and waist >=116:
        print("You are a size 8")

#end