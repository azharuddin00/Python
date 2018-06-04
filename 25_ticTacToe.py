def board(arg):
    i=0
    hor='---'
    ver='|  '
    hor=hor*arg
    ver=ver*(arg+1)
    while i <arg+1:
        print (hor)
        if not(i==arg):
            print(ver)
        i+=1


# taking board size
board_size=int(input("Enter the size of board:"))
board(board_size)
