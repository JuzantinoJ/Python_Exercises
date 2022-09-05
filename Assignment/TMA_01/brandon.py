def randshape():
    #get random choice of shape
    shapes = ['SCISSORS', 'PAPER', 'STONE']
    import random
    randomshape = random.choice(shapes)
    return randomshape

def size():
    #get size of hand
    while True:
        size = int(input('Enter size of hand: '))
        if size < 3:
            print('Please select a hand size more than 3')
        else:
            return size

def auto():
    
    autos = ['TRUE', 'FALSE']
    import random
    auto = random.choice(autos)
    return auto

def getHandOfShapes(size):
    
    size = size()
    shape = []
    for i in range(size):
        shapes = input(f'Shape {i+1}: please select a shape: ').upper()
        shape.append(shapes)
    return(shape) #remember to change back to print in answer
    
        
# def Q3b(size, shape):
    
#     glhf = getHandOfShapes(size)
#     #get random com hand of shapes
#     for x in range(3):
#         shapes = ['SCISSORS', 'PAPER', 'STONE']
#         import random
#         comchoice = random.choice(shapes)
    
#     name = input("Enter player's name: ")
#     playerscore = 0
#     comscore = 0
#     while True:
#         for s in range(3):
#             if shape == comchoice:
#                 playerscore += 0
#                 comscore += 0
#             elif shape == 'SCISSORS' and comchoice == 'PAPER':
#                 playerscore += 1
#             elif shape =='PAPER' and comchoice == 'STONE':
#                 playerscore += 1
#             elif shape =='STONE' and comchoice == 'SCISSORS':
#                 playerscore += 1
#             elif shape == 'PAPER' and comchoice == 'SCISSORS':
#                 comscore += 1
#             elif shape =='STONE' and comchoice == 'PAPER':
#                 comscore += 1
#             elif shape =='SCISSORS' and comchoice == 'STONE':
#                 comscore += 1
            
#             print(f'\nGame starts...')
#             print(f'Round {s+1}: {name} {shape} : Computer {comchoice}')
#             print(f'<< {name} {playerscore} : Computer {comscore} >>')
            
#         if playerscore == comscore:
#             print("It's a tie!! Rematch...")
#         elif playerscore > comscore:
#             print(f'{name} is the winner!!')
#         else:
#             print('Computer isthe winner!!')

# # Q3b(size, shape)
            
    
    
    
        
    
    # f'Shape {i+1}: please select a shape: ').upper()
    #     shape.append(shapes)
        
    #gethand = getHandOfShapes()
    #comchoice = comchoice()
    
    # comchoice = []
    # for i in range(size):
    #     shapes = ['SCISSORS','PAPER','STONE']
    #     import random
    #     choice = random.choice(shapes)
    #     comchoice.append(choice)
    
    # while True:
    #     playerscore = 0
    #     comscore = 0
    #     print('\nGame starts...')
    #     for s in range(size):
    #         if shape[s] == comchoice[s]:
    #             playerscore += 0
    #             comscore += 0
    #         elif shape[s] == 'SCISSORS' and comchoice[s] == 'PAPER':
    #             playerscore += 1
    #         elif shape[s] =='PAPER' and comchoice[s] == 'STONE':
    #             playerscore += 1
    #         elif shape[s] =='STONE' and comchoice[s] == 'SCISSORS':
    #             playerscore += 1
    #         elif shape[s] == 'PAPER' and comchoice[s] == 'SCISSORS':
    #             comscore += 1
    #         elif shape[s] =='STONE' and comchoice[s] == 'PAPER':
    #             comscore += 1
    #         elif shape[s] =='SCISSORS' and comchoice[s] == 'STONE':
    #             comscore += 1
            
    #         print(f'Round {s+1}: {name} {shape[s]} : Computer {comchoice[s]}')
    #         print(f'<< {name} {playerscore} : Computer {comscore} >>')
    #         print('Press <Enter> to proceed\n')
            
    #     if playerscore == comscore:
    #         print("\nIt's a tie!! Rematch...")
    #     elif playerscore > comscore:
    #         print(f'\n{name} is the winner!!')
    #         break
    #     else:
    #         print('\nComputer is the winner!!')
    #         break

def Q3c():
    while True:
        size = int(input('Enter size of hand: '))
        if size < 3:
            print('Please select a hand size more than 3')
        else:
            break
    
    name = input("Enter player's name: ")
    shape = []
    hsize = int(size/2)
    for i in range(size):
        shapes = input(f'Shape {i+1}: please select a shape: ').upper()
        shape.append(shapes)
        if shape.count('SCISSORS') > (hsize):
            print(f'Cannot have more than {hsize} SCISSORS!!')
            shapes = input(f'Shape {i+1}: please select a shape: ').upper() #help here duplicate only runs twice
            shape[hsize] = shapes
            shape[-1] = shapes
        elif shape.count('PAPER') > (hsize):
            print(f'Cannot have more than {hsize} PAPER!!')
            shapes = input(f'Shape {i+1}: please select a shape: ').upper()
            shape[hsize] = shapes
            shape[-1] = shapes
        elif shape.count('STONE') > (hsize):
            print(f'Cannot have more than {hsize} STONE!!')
            shapes = input(f'Shape {i+1}: please select a shape: ').upper()
            shape[hsize] = shapes
            shape[-1] = shapes
    
    #gethand = getHandOfShapes()
    #comchoice = comchoice()
    comchoice = []
    for i in range(size):
        shapes = ['SCISSORS','PAPER','STONE']
        import random
        choice = random.choice(shapes)
        comchoice.append(choice)
    
    while True:
        playerscore = 0
        comscore = 0
        print('\nGame starts...')
        for s in range(size):
            if shape[s] == comchoice[s]:
                playerscore += 0
                comscore += 0
            elif shape[s] == 'SCISSORS' and comchoice[s] == 'PAPER':
                playerscore += 1
            elif shape[s] =='PAPER' and comchoice[s] == 'STONE':
                playerscore += 1
            elif shape[s] =='STONE' and comchoice[s] == 'SCISSORS':
                playerscore += 1
            elif shape[s] == 'PAPER' and comchoice[s] == 'SCISSORS':
                comscore += 1
            elif shape[s] =='STONE' and comchoice[s] == 'PAPER':
                comscore += 1
            elif shape[s] =='SCISSORS' and comchoice[s] == 'STONE':
                comscore += 1
            
            print(f'Round {s+1}: {name} {shape[s]} : Computer {comchoice[s]}')
            print(f'<< {name} {playerscore} : Computer {comscore} >>')
            print('Press <Enter> to proceed\n')
        
        if playerscore > comscore:
            print(f'\n{name} is the winner!!')
            break
        elif comscore > playerscore:
            print('\nComputer is the winner!!')
            break
        else:
            print("\nIt's a tie!! Playoff...")
            x = 100
            while True:
                for s in range(x):
                    shaper = input(f'\nPlayoff {s+1}: {name}, please select a shape: ').upper()
                    print(f"Playoff {s+1}: Computer's shape is: {comchoice[0]}")
                    playscore = 0
                    compscore = 0
                    if shape == comchoice[0]:
                        playerscore += 0
                        comscore += 0
                    elif shaper == 'SCISSORS' and comchoice[0] == 'PAPER':
                        playscore += 1
                    elif shaper =='PAPER' and comchoice[0] == 'STONE':
                        playscore += 1
                    elif shaper =='STONE' and comchoice[0] == 'SCISSORS':
                        playscore += 1
                    elif shaper == 'PAPER' and comchoice[0] == 'SCISSORS':
                        compscore += 1
                    elif shaper =='STONE' and comchoice[0] == 'PAPER':
                        compscore += 1
                    elif shaper =='SCISSORS' and comchoice[0] == 'STONE':
                        compscore += 1
                    
                    print(f'<< {name} {playscore} : Computer {compscore} >>')
                    print('Press <Enter> to proceed\n')
                
                    if playscore == 1:
                        print(f'\n{name} is the winner!!')
                        return
                    elif compscore == 1:
                        print('Computer is the winner!!')
                        return
                
Q3c()