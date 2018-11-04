'''Ask the user for a number and determine whether the number is prime or not.'''



def prime(num):
    num = int(input('Give me a number to check: '))
    listrange = list(range(1, num+1))
    divisorlist = []

    for i in listrange:
        if i % listrange == 0:
            divisorlist.append(i)

    if len(divisorlist) == 0:
        print(num + ' is prime')
    else:
        print(num + ' is NOT prime')


