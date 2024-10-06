from MakePalindrome import make_palindrome

with open('../txtf/input.txt') as file:
    letters = file.readline()

with open('../txtf/output.txt', 'w') as file: 
    print(make_palindrome(letters), file=file)
