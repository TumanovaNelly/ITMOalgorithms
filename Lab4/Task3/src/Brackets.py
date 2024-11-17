from utils import read, write
from typing import List

from Lab4.Task13.src.Stack import Stack


def check_brackets(brackets: str):
    stack = Stack()
    for value in brackets:
        if value in ')]':
            if stack.is_empty(): return False

            last_opened = stack.pop()
            if value == ')' and last_opened == '[' or value == ']' and last_opened == '(':
                return False
        else:
            stack.push(value)

    return stack.is_empty()


def answer_generator(brackets_list: List[str]):
    for bracket in brackets_list:
        yield 'YES' if check_brackets(bracket) else 'NO'


def main():
    brackets_list = read(type_convert=str)
    write(end="")
    for brackets, in brackets_list:
        write('YES' if check_brackets(brackets) else 'NO', to_end=True)


if __name__ == '__main__':
    main()
