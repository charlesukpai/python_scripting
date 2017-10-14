#We are required to write a method to find the second occurence of a string t
#in the main string s

s = "De l'audace, encore de l'audace, toujours de l'audace"
t = 'audace'
#The method takes two arguements, our string and substring
def find_second(x, y):
    #first find the first occurence of the substring
    a = s.find(t)
    #add 1 to a to start the next search after the position of a, the first occurence
    b = a + 1
    #search for the next occurence specifying the search start from loaction b
    #This will return the next occurence of the substring immediately after b
    c = s.find(t, b)
    return c

print find_second(s, t)
