from operator import add, sub, mul

from Lab4.Task13.src.Stack import Stack
from utils import read, write

OPERATORS = {'+': add, '-': sub, '*': mul}


def calculate(expression: list) -> int:
    stack = Stack()
    for token in expression:
        if token in OPERATORS:
            y, x = stack.pop(), stack.pop()
            stack.push(OPERATORS[token](x, y))
        else:
            try:
                stack.push(int(token))
            except ValueError:
                raise KeyError(f'Invalid operator {token}')

    return stack.pop()


def main():
    expression, = read(type_convert=str)
    write(calculate(expression))


if __name__ == '__main__':
    main()
