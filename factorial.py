# Define a procedure, factorial, that takes one number as its input
# and returns the factorial of that number.
#This can be used to figure out the number of arrangements you can do
#for a deck with 52 cards

def factorial(n):
#set the inital value of the variable to keep track of multiplications to 1
    result = 1
#As long as n is greater than one then perform the loop
    while n >= 1:
#here we do the multiplication
        result = result * n
#Then we subtract from n to keep reducing the value
        n = n - 1
    return result

print factorial(8)
