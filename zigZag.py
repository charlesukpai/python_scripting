# This program will create a back-and-forth, zigzag pattern until the user stops it by pressing the Mu editor’s Stop button or by
# pressing ctrl -C.

#import the needed modules
import time, sys
#specifies ho many speaces to indent
indent = 0
#checks whether indetation is increasing or not.
indentIncreasing = True

try:
    #start the main program loop
    while True:
        print(' ' * indent, end='')
        print('********')
        #pause for 1/10 of a scond
        time.sleep(0.1)

        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
#handle the error by exiting the program when the user presses CTRL + C
except KeyboardInterrupt:
    sys.exit()
