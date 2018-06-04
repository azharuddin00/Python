name=input("Enter your name:")
age=int(input("Enter your age:"))
num=int(input("How many times you wish to repeat this:"))
year = str((2014 - age)+100)
i=0
while(i<num):
    if age==0:
        print("Enter a valid age")
    else:
        
        print("Hello {0} in {1} years you reach 100 in the year {2} ".format(name,100-age,year))
    i+=1
