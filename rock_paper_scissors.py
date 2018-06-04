'''

import random


def game(arg):
    a = random.choice(list1)
    if arg > a:
        print("you won", arg, a)

    elif arg < a:
        print("you lost:", arg, a)

    elif arg == a:
        print("Draw:", arg, a)


list1 = ["rock", "paper", "scissor"]
rock = "rock"
paper = "paper"
scissor = "scissor"
rock > scissor
scissor > paper
paper > rock
ask = input("Do you want to play [y/n]:")

if ask == 'y':
    while ('y'):
        arg = input("Enter rock/paper/scissor:")
        game(arg)
else:
    exit(0)

'''

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))


