# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = eval(input("Enter a list in the form :[(2, 2), (3, 4), (4, 1), (1, 3)]: "))

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
