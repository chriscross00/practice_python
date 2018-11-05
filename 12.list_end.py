'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
list of only the first and last elements of the given list. For practice, write this code inside a
function.'''

a = [5, 10, 15, 20, 25]

x = a[0]
y = a[-1]
z = [x, y]

print(z)

#As a function
a = [0, 10, 15, 20, 29]

def firstlast (list):
    z = [list[0], list[-1]]
    return(z)

print(firstlast(a))