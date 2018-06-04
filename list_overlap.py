'''
list1=eval(input("Enter another list in the form [1,2,3]  :"))
list2=eval(input("Enter another list in the form [1,2,3]  :"))
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)
'''

import random
c=[]
a=range(1,random.randint(1,30))
b=range(1,random.randint(1,40))
for i in a:
    if i in b:
        c.append(i)
print(c)

'''

import random
a = range(1, 100)
b = range(1, 50)

commonList = set();

[commonList.add(x) for x in a for y in b if x == y]

print(list(commonList))

'''


