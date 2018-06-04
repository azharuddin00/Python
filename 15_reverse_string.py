def reverse_v4(x):
    y = x.split()
    z=y[::-1]
    result=[]
    for i in z:
        result.append(i)
    return " ".join(result)
test=input("Enter a String:")
print(reverse_v4(test))
