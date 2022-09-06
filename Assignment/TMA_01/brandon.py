def readSeatingPlan(filename): 
    lgd = ['O','X','#'] 
    dic = {} 
    f = open(filename, "r") 
    for x in f: 
        splt = x.split(',', 1) 
        seats = splt[-1] 
        sl = [x for x in [*seats] if x in lgd] 
        dic[splt[0]] = sl 
    return dic 
 
readSeatingPlan("Monkey Goes East-202209081430.txt") 
 
def showSeatingPlan(seatingPlan): 
    lgd = ['O','X','#'] 
    ssize = -1 
    for k,v in seatingPlan.items(): 
        siz = len(v) 
        if siz > ssize: ssize = siz 
        seats = str(v) 
        s = '  '.join(filter(lambda x: x in lgd, seats)) 
        print(f'{k}  {s}') 
    print(' ', end=' ') 
    for i in range(ssize): print(str(i+1).zfill(2), end=' ') 
     
 
####################################################### 
def getFilenameInfo(filename): 
    d = {} 
    splt = filename.split('.', 1)[0].split('-', 1) 
    d['filename'] = filename.strip() 
    d['title'] = splt[0] 
    date = splt[-1][:8] 
    time = splt[-1].replace(date,'') 
    d['date'] = f'{date[:4]}-{date[4:6]}-{date[6:8]}' 
    d['time'] = f'{time[:2]}:{time[2:]}' 
    return d 
getFilenameInfo("FR_Productions.txt") 
 
 
def getMenuSelection(title, optionList, menuType): 
    selectionTxt = 'Enter selection: ' if menuType == 'M' else 'Enter option: ' 
    xTxt = 'Exit' if menuType == 'M' else 'Back to Main Menu' 
    print(title) 
     
    for i,e in enumerate(optionList): 
        print(f'{i+1}. {e}') 
    print(f'X. {xTxt}') 
     
    while True: 
        i_sel = str(input(selectionTxt)) 
        if i_sel.isdigit(): 
            i_sel_conv = int(i_sel)-1 
            if i_sel_conv < len(optionList) and i_sel_conv >= 0: return int(i_sel)-1 
            else: print(f'Selection is out of range...') 
        else:  
            if i_sel.upper() == 'X': return 'EXIT' if menuType == 'M' else 'MAIN'  
            else:  
                print('Selection is not valid...')  
                continue 
 
 
 
def validateBookSeats(seatsDic, bookSelectionList): 
    excpt = False 
    for x in bookSelectionList: 
        r = x[:1] 
        c = int(x[1:])-1 
        seatVal = seatsDic[r][c] 
        if seatVal == "O": 
            seatsDic[r][c] = 'X' 
        elif seatVal == "X": 
            print(f"Exception!! {x} is BOOKED") 
            excpt = True 
        else: 
            print(f"Exception!! {x} is BLOCKED") 
            excpt = True 
    if excpt: return "EXCEPTION" 
    else: return seatsDic 
# showSeatingPlan(validateBookSeats(readSeatingPlan("Monkey Goes East-202209081430.txt"), ["B1", "E9"])) 
 
def validateCancelSeats(seatsDic, cancelSelectionList): 
    excpt = False 
    for x in cancelSelectionList: 
        r = x[:1] 
        c = int(x[1:])-1 
        seatVal = seatsDic[r][c] 
        if seatVal == "X": 
            seatsDic[r][c] = 'O' 
        elif seatVal == "O": 
            print(f"Exception!! {x} is not booked") 
            excpt = True 
        else: 
            print(f"Exception!! {x} is BLOCKED") 
            excpt = True 
    if excpt: return "EXCEPTION" 
    else: return seatsDic 
 
 
def transformToFileFormat(seatDic): 
    lgd = ['O','X','#'] 
    res = [] 
    for k,v in seatDic.items(): 
        strg = str(v) 
        conv = ''.join(filter(lambda e: e in lgd, strg)) 
        res.append(f'{k}, {conv}\n') 
    return res 
 
 
################################# 
def rewriteFileData(filename, dataList): 
    file = open(filename,'w') 
    file.writelines(dataList) 
    file.close() 
     
isExit = False 
while not isExit: 
    filename = "FR_Productions.txt" 
    f = open(filename, "r") 
    mainLi = [] 
    txtLi = [] 
 
    for i,x in enumerate(f): 
        fileInfo = getFilenameInfo(x) 
        txt = f'{fileInfo["title"]} @ {fileInfo["date"]} {fileInfo["time"]}' 
        mainLi.append(fileInfo) 
        txtLi.append(txt) 
 
    i_sel = getMenuSelection("\nMain Menu - FR Productions\n==========================", txtLi, "M")    
    if i_sel == 'EXIT':  
        isExit = not isExit
        continue 
 
    #display the production title, performance datetime, seating plan and the sub-menu 
    while True: 
        selected = mainLi[i_sel] 
        print(f'\nProduction: {selected["title"]}') 
        print(f'Performance datetime: {selected["date"]} {selected["time"]}') 
        print(f'Seating plan:') 
        showSeatingPlan(readSeatingPlan(selected["filename"])) 
 
     
     
        subMenuLi = ["Book Seats", "Cancel Bookings"] 
        i_subSel = getMenuSelection("\n\nSub-Menu\n========", subMenuLi, "S") 
        if i_subSel == 'MAIN': break 
        else: 
            selSeatDic = readSeatingPlan(mainLi[i_sel]['filename']) 
            # Book seats (option 1) 
            if i_subSel == 0: 
                i_seats = str(input("Enter seats to book: ")) 
                selSeatsSplt = i_seats.split(',') 
                res = validateBookSeats(selSeatDic, selSeatsSplt) 
                if res == "EXCEPTION":  
                    print("This booking is aborted") 
                    continue 
                else: print(f"Booking of {i_seats} done") 
            # Cancel Bookings (option 2) 
            else: 
                i_seats = str(input("Enter seats to cancel: "))   
                selSeatsSplt = i_seats.split(',') 
                res = validateCancelSeats(selSeatDic, selSeatsSplt) 
                if res == "EXCEPTION":  
                    print("This cancellation is aborted") 
                    continue 
                else: print(f"Cancellation of booking for {i_seats} done") 
             
            fileData = transformToFileFormat(res) 
            rewriteFileData(mainLi[i_sel]['filename'], fileData)