


def ispresent(arg,b):
    for i in arg:
        if i==b:
            return True
        else:
            return False




a=eval(input("Enter a list in the form [1,2,3]:"))
a.sort()
b=int(input("Enter  a Number:"))
print(ispresent(a,b))
