#Question 1 (b)
# (b) Using Table 1-2, write a program to recommend the T-Shirt size, based on customers’ 
# height,  chest,  and  waist  measurements.  Your  program  must  display  the  appropriate 
# “fitting” based on the following fitting rules: 
# o best fit: if all three measurements indicate same size. 
# o regular  fit:  if  two  measurements  indicate  same  larger  size  than  the  third.  See 
# Sample execution 2 below. 
# o relaxed  fit:  if  one  measurement  indicates  larger  size  than  the  other  two.  See 
# sample execution 3 below. 
 
# Assume user will enter valid input. 
#create variable for 3 inputs - Height ,Chest and Weight

height = int(input("Enter height : "))
chest = int(input("Enter chest: "))
waist = int(input("Enter waist: "))

if height < 155 and chest < 80 and waist < 70:
    print("You are size 1 (best fit)")
elif height <= 155 and chest >= 80 and chest < 88 and waist >= 70 and waist < 76: #chest and waist greater than height
    print("You are size 2 (regular fit)")
elif waist <= 70 and height >= 155 and height < 160 and chest >= 80 and chest >= 88  : #height and chest greater than waist 
    print("You are size 2 (regular fit)")
elif chest <= 80 and height >= 155 and height < 160   and waist >= 70 and waist < 76: #height and waist greater than chest
    print("You are size 2 (regular fit")
elif height >= 155 and height < 160 and chest < 80 and waist < 70: #height is greater than chest and weight
    print("You are size 2 (relaxed fit)")
elif chest >= 80 and chest < 88 and height < 155 and waist < 70: # chest is greater than height and waist
    print("You are size 2 (relaxed fit)")
elif waist >= 70 and waist < 76 and chest < 80 and height < 155: # waist is greater than chest and height
    print("You are size 2 (relaxed fit)")

if height >= 155 and height < 160 and chest >= 80 and chest < 88 and waist >= 70 and waist < 76:
    print("You are size 2 (best fit)")
elif height >= 155 and height < 160 and chest >= 88 and chest < 96 and waist >= 76 and waist < 84: #chest and waist greater than height
    print("You are size 3 (regular fit)")
elif waist >= 70 and waist < 76 and height >= 160 and height < 165 and chest >= 88 and chest >= 96  : #height and chest greater than waist 
    print("You are size 3 (regular fit)")
elif chest >= 80 and chest < 88 and height >= 160 and height < 165   and waist >= 76 and waist < 84: #height and waist greater than chest
    print("You are size 3 (regular fit")
elif height >= 160 and height < 165 and chest < 88 and waist < 76: #height is greater than chest and weight
    print("You are size 3 (relaxed fit)")
elif chest >= 88 and chest < 96 and height < 160 and waist < 76: # chest is greater than height and waist
    print("You are size 3 (relaxed fit)")
elif waist >= 76 and waist < 84 and chest < 88 and height < 160: # waist is greater than chest and height
    print("You are size 3 (relaxed fit)")


if height >= 160 and height < 165 and chest >= 88 and chest < 96 and waist >= 76 and waist < 84:
    print("You are size 3 (best fit)")
elif height >= 160 and height < 165 and chest >= 96 and chest < 104 and waist >= 84 and waist < 92: #chest and waist greater than height
    print("You are size 4 (regular fit)")
elif waist >= 76 and waist < 84 and height >= 165 and height < 170 and chest >= 96 and chest >= 104  : #height and chest greater than waist 
    print("You are size 4 (regular fit)")
elif chest >= 88 and chest < 96 and height >= 165 and height < 170   and waist >= 84 and waist < 92: #height and waist greater than chest
    print("You are size 4 (regular fit")
elif height >= 165 and height < 170 and chest < 96 and waist < 84: #height is greater than chest and weight
    print("You are size 4 (relaxed fit)")
elif chest >= 96 and chest < 104 and height < 165 and waist < 84: # chest is greater than height and waist
    print("You are size 4 (relaxed fit)")
elif waist >= 84 and waist < 92 and chest < 96 and height < 165: # waist is greater than chest and height
    print("You are size 4 (relaxed fit)")


if height >= 165 and height < 170 and chest >=96 and chest < 104 and waist >=84 and waist < 92:
    print("You are size 4 (best fit)")
elif height >= 165 and height < 170 and chest >= 104 and chest < 112 and waist >= 92 and waist < 100: #chest and waist greater than height
    print("You are size 5 (regular fit)")
elif waist >= 84 and waist < 92 and height >= 170 and height < 175 and chest >= 104 and chest >= 112  : #height and chest greater than waist 
    print("You are size 5 (regular fit)")
elif chest >= 96 and chest < 104 and height >= 170 and height < 175   and waist >= 92 and waist < 100: #height and waist greater than chest
    print("You are size 5 (regular fit")
elif height >= 170 and height < 175 and chest < 104 and waist < 92: #height is greater than chest and weight
    print("You are size 5 (relaxed fit)")
elif chest >= 104 and chest < 112 and height < 170 and waist < 92:
    print("You are size 5 (relaxed fit)")
elif waist >= 92 and waist < 100 and chest < 112 and height < 170:
    print("You are size 5 (relaxed fit)")


if height >=170 and height < 175 and chest >= 104 and chest < 112 and waist >= 92 and waist < 100:
    print("You are size 5 (best fit)")
elif height >= 170 and height < 175 and chest >= 112 and chest < 120 and waist >= 100 and waist < 108: #chest and waist greater than height
    print("You are size 6 (regular fit)")
elif waist >= 92 and waist < 100 and height >= 175 and height < 180 and chest >= 112 and chest >= 120  : #height and chest greater than waist 
    print("You are size 6 (regular fit)")
elif chest >= 104 and chest < 112 and height >= 175 and height < 180   and waist >= 100 and waist < 108: #height and waist greater than chest
    print("You are size 6 (regular fit")
elif height >= 175 and height < 180 and chest < 175 and waist < 100: #height is greater than chest and weight
    print("You are size 6 (relaxed fit)")
elif chest >= 112 and chest < 120 and height < 175 and waist < 100: # chest is greater than height and waist
    print("You are size 6 (relaxed fit)")
elif waist >= 100 and waist < 108 and chest < 112 and height < 175: # waist is greater than chest and height
    print("You are size 6 (relaxed fit)")

if height >= 175 and height < 180 and chest >= 112 and chest < 120 and waist >= 100 and waist < 108:
    print("You are size 6 (best fit)")
elif height >= 175 and height < 180 and chest >= 120 and chest < 128 and waist >= 108 and waist < 116: #chest and waist greater than height
    print("You are size 7 (regular fit)")
elif waist >= 100 and waist < 108 and height >= 180 and height < 185 and chest >= 120 and chest >= 128  : #height and chest greater than waist 
    print("You are size 7 (regular fit)")
elif chest >= 112 and chest < 120 and height >= 180 and height < 185   and waist >= 108 and waist < 116: #height and waist greater than chest
    print("You are size 7 (regular fit")
elif height >= 180 and height < 185 and chest < 120 and waist < 108: #height is greater than chest and weight
    print("You are size 7 (relaxed fit)")
elif chest >= 120 and chest < 128 and height < 180 and waist < 108: # chest is greater than height and waist
    print("You are size 7 (relaxed fit)")
elif waist >= 108 and waist < 116 and chest < 120 and height < 180: # waist is greater than chest and height
    print("You are size 7 (relaxed fit)")

if height >= 180 and height < 185 and chest >=120 and chest < 128 and waist >=108 and waist < 116:
    print("You are size 7 (best fit)")

if height > 185 and chest > 128 and waist > 116:
    print("You are size 8.")

#end