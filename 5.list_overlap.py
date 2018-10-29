'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python'''

#create both list
#if else statement, if i in a and i in b, then return c[i]
#else return nothin

#note: this is not a very elegant solution, it takes N*M time

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b:
        c.append(i)

c = list(set(c))
print(c)

#Extra 1
x = []
y = []
for i in range(10):
    x.append(random.randint(1, 101))
    y.append(random.randint(1, 101))
print(x)
print(y)


'''This is a really cool implementation that somebody else did, also using sets. It's a lot cleaner.
import random   
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 10)

commonList = set();

[commonList.add(x) for x in a for y in b if x == y]

print(list(commonList))'''
