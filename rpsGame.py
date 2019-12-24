#creating a rock paper scissors game where user plays the computer:

#first we import the modules we need
import random, sys

print('ROCK, PAPER, SCISSORS')

#Define variables to keep track of numbr of wins, losses and ties.
wins = 0
losses = 0
ties = 0

#Create the main game loop:
while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
#next the player input loop:
    while True:
        print('Enter your move: (r)rock | (p)paper | (s)scissors or (q)quit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #exits the game once the player types q.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        #breaks out of the player input loop
        print('Type one of r, p, s or q.')

    #Displaying the user selections:
    if playerMove == 'r':
        print('ROCK versus.....')
    elif playerMove == 'p':
        print('PAPER versus.....')
    elif playerMove == 's':
        print('SCISSORS versus.....')

    #Displaying the computer's selection:

    #computer will pick random numbers between 1 -3 to represent it's input:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #Display the results and record them:
    if playerMove == computerMove:
        print('We have a Tie.!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win.!!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win..!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win..!!')
        wins = wins + 1
    elif playerMove =='r' and computerMove == 'p':
        print('You lose..!!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose..!!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose..!!')
        losses = losses + 1


