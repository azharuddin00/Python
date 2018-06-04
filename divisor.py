num=int(input("Enter a number:"))
x=range(1,num+1)
list=[]
for elem in x:
    if(num%elem==0):
        list.append(elem)
print(list)
