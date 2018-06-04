import os,sys
print(os.getcwd())
name=input("Enter a string:")
for alphabet in name:
    if alphabet.islower()==True:
        print(alphabet.upper(),end='')
    else:
        print(alphabet.lower(),end='')
    
