# Define a method, bigger, that takes in two numbers as inputs,
#and returns the greater of the two inputs.

def bigger(x, y):
    if x > y:
        ans = x
    else:
        ans = y
    return ans

print bigger(2, 7)
