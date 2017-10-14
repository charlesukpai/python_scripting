# Define a function, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    #first set your start point or the loop
    i = 1
    #while 1 is less than or equal to n.
    #This will print out iuntil i = n
    while i <= n:
        print i
        #This increments the loop to ensure it doesnt go on infinitely
        i = i + 1

print_numbers(20)

#Another way to write this:

# def print_numbers(n):
#     i = 0
#     while i < n:
#         i = i + 1
#         print i
