'''Ask the user for a number and determine whether the number is prime or not.'''

num = int(input('Give me a number to check: '))

def prime(num):
    listrange = list(range(1, num+1))
    divisorlist = []

    for i in listrange:
        if num % i == 0:
            divisorlist.append(i)

    if len(divisorlist) == 2:
        print(str(num) + ' is prime')
    else:
        print(str(num) + ' is NOT prime')


prime(num)


