from utils import read, write


def fib(n):
    last1, last2 = 0, 1
    for _ in range(n):
        last1, last2 = last2, (last1 + last2) % 10

    return last1


def main():
    (n, ), = read()
    if 0 <= n <= 45:
        write(fib(n))
    else: print('Incorrect numbers. Try again.')


if __name__ == '__main__':
    main()