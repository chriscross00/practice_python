'''Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using
sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.'''
import random

#repeated = random.sample(range(1,20), 18)
repeated = [1,4,6,2,5,6,2,1,6,7,8,65,8,9,7]

def unqiue(x):
    return list(set(x))
#print(repeated)
print(unqiue(repeated))

#Extra 1
repeated = [1,4,6,2,5,6,2,1,6,7,8,65,8,9,7]
def unique(listed):
    unique_list = []
    for i in repeated:
        if i not in unique_list:
            unique_list.append(i)
    return(unique_list)

print(unique(repeated))