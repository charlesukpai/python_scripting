# Define a procedure, is_friend, that takes a string as its input, and
# returns a Boolean indicating if the input string is the name of
# a friend. Assume I am friends with everyone whose name starts with D
# and no one else. You do not need to check for the lower case 'd'

def is_friend(name):
#this checks if the first letter of each string starts with D
    if s[0] == 'D':
        x = s[0] == 'D'
    else:
#for strings not starting with D this will evaluate to false
        x = s[0] == 'D'
    return x
print is_friend('Dred')

#This can be written in a much simpler form as:

#def is_friend(name):
    #return s[0] == 'D'
