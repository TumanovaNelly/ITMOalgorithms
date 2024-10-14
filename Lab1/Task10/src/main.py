from MakePalindrome import make_palindrome

def main():
    with open('../txtf/input.txt') as file:
        letters = file.readline()

    with open('../txtf/output.txt', 'w') as file: 
        print(make_palindrome(letters), file=file)

if __name__ == "__main__":
    main()
