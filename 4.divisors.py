''''Create a program that asks the user for a number and then prints out a list of all the divisors
of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another
number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

#create range of(0, 10000)
#ask user for input
#for loop ask if range is divisor
#print list

num = int(input('Give me a number to divide: '))
listrange = list(range(1,num+1))

divisorlist = []

for i in listrange:
    if num % i == 0:
        divisorlist.append(i)

print(divisorlist)
