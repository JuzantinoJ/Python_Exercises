


def bookSeat():
    seats_chose = []
    row = []
    seat = []
    seats_to_book = input("Enter seats to book: ").upper()
    seats_chose.append(seats_to_book.split(','))
    for i in seats_chose:
        for x in i:
            z= x[0]
            y= x[1]
            row.append(z)
            seat.append(y)
    dict_list = [dict(zip(row, i)) for i in seat]
    print(type(dict_list))
bookSeat()

