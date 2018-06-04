import random as r
l=[]
def pick(arg):
    word=r.choice(arg)
    return word
with open("dict.txt",'r') as d:
    line=d.readline()
    while line:
        line=line.strip()
        l.append(line)
        line=d.readline()

if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = pick(l)
	guessed = "_" * len(word)
	word = list(word)
	guessed = list(guessed)
	lstGuessed= []
	letter = input("guess letter: ")
	while True:
		if letter.upper() in lstGuessed:
			letter = ''
			print("Already guessed!!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter is not '':
				lstGuessed.append(letter.upper())
			letter = input("guess letter: ")

		if '_' not in guessed:
		    print("You won!!")
		    
		    
		    break
