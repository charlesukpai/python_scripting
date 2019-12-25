# Conway's Game of Life:
########################
# Conway’s Game of Life is an example of cellular automata: a set of rules governing the behavior of a field made up of discrete cells.
# We can use a list of lists to represent the two-dimensional field. The inner list represents each column of squares and stores a '#' hash string for
# living squares and a ' ' space string for dead squares.

import random, time, copy

width = 60
height = 20

#create list of lists for the cells:
nextCells = []

for x in range(width):
    column = [] #creates a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') #This adds a living cell.
        else:
            column.append(' ')#this adds a dead cell

    nextCells.append(column) #This is a list of column lists

#begnging of the main program loop:
while True:
    print('\n\n\n\n\n') #this seperates each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    #print the current cells on the screen
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='')#print the # or the ' '
        print() # this prints a new line at the end of the row
    
    #next, calculate the next step's cells based on the current step's cells:
    for x in range(width):
        for y in range(height):
            #get the neighbouring cell's coordinates
            #the % width ensures that the leftCoord is always between 0 and width - 1.
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            #Counting the number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #top left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 #top right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 #right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 #Bottom left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 #bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom right neighbor is alive
            
            #Next set cells based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] == '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #dead cells with 3 neighbors come alive:
                nextCells[x][y] == '#'
            else:
                #everything else dies or stays dead if already dead:
                nextCells[x][y]= ' '
    time.sleep(1) #Add a one second pause to reduce flickering.



