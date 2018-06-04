word='azhar'
guessed='_'*len(word)
guess=[]
guessed=list(guessed)
word=list(word)
letter=input("guess a letter:")
while True:
    if letter.upper() in guess:
        letter=''
        print("already guessed")
    elif letter.upper() in word:
        index=word.index(letter.upper())
        guessed[index]=letter.upper()
        word[index]='_'
    else:
        print(''.join(guessed))
        if letter is not '':
            guess.append(letter.upper())
        letter=input("guess letter:")
    if '_' not in guessed:
        print("You Won")
        break
