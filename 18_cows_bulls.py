import random as r
def cow(arg):
    cow=0
    bull=0
    a=str(list(range(1,9)))
    print(a)
    for x in arg:
    
        for i in a:
            if x in a and x==a[i]:
                cow+=1
            elif 'x' in a:
                bull+=1
    return ("cow= {},bull={}".format(cow,bull))

if __name__=='__main__':
    z=input("Enter a 4 digit number:")
    print(cow(z))
    #print("bulls={0},cows={1}".format(cow.bull,cow.cow))
