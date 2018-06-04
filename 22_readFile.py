counter={}
with open("names.txt",'r') as file:
    line=file.readline()
    while line:
        line=line.strip()
        if line in counter:
            counter[line]+=1
        else:
            counter[line]=1
        line=file.readline()
print(counter)
