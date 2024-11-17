from Lab4.Task13.src.Stack import Stack
from utils import read, write


def main():
    stack = Stack()
    write(end="")
    for line in read(type_convert=str):
        if line[0] == '+':
            stack.push(line[1])
        elif line[0] == '-':
            write(stack.pop(), to_end=True)
        else:
            raise ValueError('Invalid input')


if __name__ == '__main__':
    main()
