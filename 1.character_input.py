'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn
100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message. (Hint: order of operations exists in Py)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime

name = input('Give me your name: ')
age = int(input('Give me your age: '))
turn = (100-age) + datetime.date.today().year

print( name + ' will turn 100 in ' + str(turn))

#Extra 1
num = int(input('Give me another number: '))

print( num*(name + ' will turn 100 in ' + str(turn)))

#Extra 2
for i in range(num):
    print(name + ' will turn 100 in ' + str(turn))