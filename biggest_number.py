# Define a procedure, biggest, that takes three numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
#The first if statement checks if a is greater than or equal to either b or c
    if a >= b and a >= c:
        return a
#the else if statement checks if b is greater than or equal to either a or c
    elif b >= a and b >= c:
        return b
#The last else if checks if c is greater than or equal to either a or b
    elif c >= a and c >= b:
        return c
    #If none if this is true we return to the start
    else:
        return
print biggest(2, 2, 1)


#You can write a very simple version of this using the max method in python:
#def biggest(a, b, c):
    #return max(a, b, c)
