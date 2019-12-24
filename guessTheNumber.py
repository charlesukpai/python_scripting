#This program makes you guess a number.

#first we import the random module to generate random numbers between 1 - 20:
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20 ')

#Ask the player to make 6 guesses:
for guessTaken in range(1, 7):
    print('make a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low, try again')
    elif guess > secretNumber:
        print('Your guess is too high, try again')
    else:
        break #breaks if they guess the right answer.

if guess == secretNumber:
    print('Good job! You guessed the correct number in ' + str(guessTaken) + ' guesses!')
    #else statement kicks in once they have made 6 wrong guesses.   
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))
