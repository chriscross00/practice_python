'''Ask the user for a number. Depending on whether the number is even or odd, print out an
appropriate message to the user. Hint: how does an even / odd number react differently when
divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by
(check). If check divides evenly into num, tell that to the user. If not, print a different
appropriate message.'''

num = int(input('Give me a number: '))

if num % 2 == 0:
    print(str(num) + ' is even')
else:
    print(str(num) + ' is odd')

#Extra 1
num = int(input('Give me a number: '))

if num == 4:
    print(str(num) + ' your number is 4, duh')
elif num % 2 == 0:
    print(str(num) + ' is even')
else:
    print(str(num) + ' is odd')

#Extra 2
num = int(input('Give me a number to divide: '))
check = int(input('Give me a number to divide by: '))

if num % check == 0:
    print(str(check) + ' divides ' + str(num))
else:
    print(str(check) + ' does not divides ' + str(num))