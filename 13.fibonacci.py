'''Write a program that asks the user how many Fiboncci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
the number of numbers in the sequence to generate.'''

#Ask user for input
#Create fibonacci function
#apply fib() on user num

fib_input = int(input('Length of Fibonnci sequence: '))

def fib(num):
    if num < 0:
        print('Please give a number greater than 0')
    if num <= 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)


print(fib(fib_input))