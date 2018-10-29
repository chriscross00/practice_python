''''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

a = [1, 2, 3, 2, 1, 7]

if a[:] == a[::-1]:
    print(True)
else:
    print(False)

#Ask for user input
#Because strings are list, use above ifelse statement
#Return if palindrome

word = input('Insert a word: ')
if word[:] == word[::-1]:
    print('Your word is a palindrome')
else:
    print('Your word is NOT a palindrone')

