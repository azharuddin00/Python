import random as r
b=[]
a=range(1,10)
def listends(arg):

    b.append(arg[0])
    if len(arg)>2:
        b.append(len(arg)-1)

listends(a)
print(b)
