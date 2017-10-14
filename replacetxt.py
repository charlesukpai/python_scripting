# Write a program that takes a line of text and
# finds the first occurrence of a certain marker
# and replaces it with a replacement text.
# The resulting line of text should be stored in a variable.
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."


# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

#s locates the occurence of our marker
s = line.find(marker)
#y gives us the length of the marker string
y = len(marker)
#z subtracts one to count the whole string since the first location is already s
z = len(marker) - 1
a = s + z
#the 1 arguement in the replace function specifies we are only replacing the first occurence of the marker
#to replace all occurences we use a instead of 1
replaced = line.replace(marker, replacement, 1)
print replaced
