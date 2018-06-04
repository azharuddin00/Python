list1=[]
list2=[]

with open("1.txt",'r') as f1:
    line=f1.readline()
    for line in f1:
        line=line.strip()
        list1.append(int(line))
with open("2.txt",'r') as f2:
    line=f2.readline()
    for line in f2:
        line=line.strip()
        list2.append(int(line))

list3=[x for x in list1 if x in list2]
print("\n\n\n\n\n",list1)
print("\n\n\n\n\n",list2)
print("\n\n\n\n\n",list3)
