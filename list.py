list=eval(input("Enter  a list in the form [1,2,3]  :"))
num=eval(input("enter a number to check:"))
list1=[]
for item in list:
    if item<num:
        list1.append(item)

print(list1)

