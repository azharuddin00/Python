
import random

'''
list1=range(1,random.randint(1,100))
list2=[]
for i in list1:
   if i%2==0:
       list2.append(i)
print(list2)
'''
'''
import random
list1=range(1,random.randint(1,100))
list2=list(filter(lambda x:x%2==0,list1))

print(list2)
'''

a = range(1,random.randint(1,100))
b = [number for number in a if number % 2 == 0]

print(b)
