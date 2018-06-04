a=eval(input("Enter a list in the form [1,2,3,]  :"))
b=eval(input("Enter a list in the form [1,2,3,]  :"))

c=[x for x in a if x in b]
##c=[]
##for x in a:
##    if x in b:
##        c.append(x)
print(c)
