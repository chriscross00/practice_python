'''Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the
lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
c = [i for i in a for j in b if i == j]
c = list(set(c))
print(c)

#Test on list of different sizes
import random

x = random.sample(range(1, 100), 20)
y = random.sample(range(1, 100), 14)

z = []
z = [i for i in x for j in y if i == j]
z = list(set(z))
print('This is list x: ' + str(x))
print('This is list y: ' + str(y))
print(z)


