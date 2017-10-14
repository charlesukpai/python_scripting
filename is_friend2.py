# Define a method, is_friends, that takes a string as its input, and returns a
# Boolean indicating if the input string is the name of a friend. Assume
# I am friends with everyone whose name starts with either 'D' or 'N', but no one
# else. You do not need to check for lower case 'd' or 'n'

s = raw_input('Enter a name: ')

def is_friends(s):
    if (s[0] == 'D') or (s[0] == 'N'):
        return True
    else:
        return False
print is_friends(s)


#A short way of writing the same code using 'or' would be:

# name = raw_input('Enter a name: ')
#  def is_friends(name):
#      return name[0] == 'D' or name[0] == 'N'
#
#  print is_friends(name)
