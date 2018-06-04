matrix=[
    [2,2,0],
    [2,1,0],
    [2,1,1]

    ]

def lat():
    if matrix[0][0]==matrix[0][1]==matrix[0][2]:
        print("user win")
    if matrix[1][0]==matrix[1][1]==matrix[1][2]:
        print("user win")
    if matrix[2][0]==matrix[2][1]==matrix[2][2]:
        print("user win")

def ver():
    if matrix[0][0]==matrix[1][0]==matrix[2][0]:
        print("User win")
    if matrix[0][1]==matrix[1][1]==matrix[2][1]:
        print("User win")
    if matrix[0][2]==matrix[1][2]==matrix[2][2]:
        print("User win")

def diagonal():
        

