from utils import read, write


def main():
    (a, b), = read()
    if -(10 ** 9) <= a <= (10 ** 9) and -(10 ** 9) <= b <= (10 ** 9):
        write(a + b ** 2)


if __name__ == '__main__':
    main()