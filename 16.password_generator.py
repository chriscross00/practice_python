'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a
main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a
list.'''


#ok, so create 3 functions: strong password, weak password, and return password from user input.
import random
import string

def strong(N = 12, chars = string.hexdigits + string.punctuation + string.ascii_letters):
    return ''.join(random.choice(chars) for i in range(N))

def weak():
    words = ['password', 'passwood', 'password1234', 'home1234', 'moviescreen', 'simple', 'words0987']
    return random.choice(words)

user = input('Choose password strength (STRONG/WEAK): ')
def password(user):
    if user == 'STRONG':
        return strong()
    elif user == 'WEAK':
        return weak()
    else:
        print('Please pick a option')

print(password(user))