from Lab1.Task10.src.MakePalindrome import make_palindrome
from Utils.Read_n_Write import read, write


def main():
    letters, = read(type_convert=str)
    write(make_palindrome(*letters))


if __name__ == "__main__":
    main()
