#we import the sys module.
import sys
# Practice Project:
#############################################################################################
#(1.)
# Write a function named collatz() that has one parameter named number. If number is even, 
# then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

# Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

#the collatz function is defined here:
def collatz(number):
    #checks if the number is divisible by 2 and if so prints and returns the number.
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    #checks if the number is odd and not divisible by 2
    #prints and returns the value of r.
    elif number % 2 == 1:
        r = 3 * number + 1
        print(r)
        return r

#################################################################################################
#(2.)
# Then write a program that lets the user type in an integer and that
# keeps calling collatz() on that number until the function returns the value 1.
#add an exception rule to handle what happens when someone enters an invalid value.

#A notice to the user on how they can exit the program.
print('NOTE: - Press CTRL + C to exit at any time..!!!')

print() #gives a space between lines to make the output cleaner
try: #the start of our error handling for when users press CTRL + C
    while True:
        try: #our second error handling for when a user enters a non-integer value e.g a string
            chooseNumber = int(input('Enter a valid integer: '))
            
            
            while chooseNumber != 1:
                chooseNumber = collatz(chooseNumber)
                continue
        #handles the error for wrong input and asks the user for the correct input.
        except ValueError:
            print('That is not a valid integer, please enter a valid integer :-)')
#handles the error thrown by exiting the program when the user presses CTRL + C.
except KeyboardInterrupt:
    sys.exit()#allows us exit the program when the user hits CTRL + C
