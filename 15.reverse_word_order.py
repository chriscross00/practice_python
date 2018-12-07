'''Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.'''

#Ask user for input
#Set up reverse stirng function
    #split string along spaces
    #use reverse function
    #print

user_string = input('Give me a string to reverse: ')

def reverse_string(str):
    split_str = str.split()
    split_str.reverse()
    return ' '.join(split_str)

print(reverse_string(user_string))

#Short function
user_string = input('Give me a string to reverse: ')
def reverseword(W):
    return ' '.join(W.split()[::-1])
print(reverseword(user_string))
