import random as r
##user=int(input("Enter a number:"))
print("This is a guessing game")
print("Guess a no b/w 1 to 10")
i=1
count=0
comp=r.randint(1,10)
print("The computer Guessed No is : {} ".format(comp))
print("if it is lower type 'l' ",end=(','))
print("if it is higher then type 'h' ",end=(','))
print("for exit type 'e' ",end=(','))
print("for yes type 'y'",end=('\n'))
while(i):
    
    choice=input("[l/h/e/y] : ")
    if choice=='e':
        exit(0)
    elif choice=='l':
        print("The computer Guessed No is : {} ".format(r.randint(1,comp)))
    elif choice=='h':
        print("The computer Guessed No is : {} ".format(r.randint(comp,10)))
    elif choice=='y':
        i-=1
    count+=1
print("times tried:", count)
