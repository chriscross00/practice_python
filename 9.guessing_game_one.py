'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the
user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

#Try 1.1
#import random
#create number to guess
#ask for user input
#if-else statements

#Try 1.2
#Import random
#Create while loop
#Repeat above

import random
num = random.randint(1,9)

while True:
    guess = int(input('Guess the number: '))
    if num == guess:
        print('You guessed correctly!')
        if str(input('Do you want to continue: Yes/Exit?\n')) == 'Exit':
            break
        else:
            continue
    elif num > guess:
        print('You are too low')
    elif num < guess:
        print('You are too high')

import random
rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()