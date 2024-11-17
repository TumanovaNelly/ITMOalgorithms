from typing import TypeVar

from Lab4.Task13.src.SingleLinkedList import SingleLinkedList
from utils import read, write

T = TypeVar('T')


class MinusInfinity:
    def __lt__(self, number: int) -> bool:
        return True

    def __gt__(self, number: int) -> bool:
        return False

    def __sub__(self, number: int):
        return self

    def __add__(self, number: int):
        return self


class Stack:
    def __init__(self):
        self.stack = SingleLinkedList()
        self.__mx = MinusInfinity()

    def push(self, value: int) -> None:
        self.stack.push(self.__mx - value)
        if self.__mx < value:
            self.__mx = value

    def pop(self) -> T:
        removed_value = self.stack.pop()

        return_value = self.__mx
        if removed_value < 0:
            self.__mx = removed_value + self.__mx
        else:
            return_value -= removed_value

        return return_value

    def max(self):
        if len(self.stack) == 0:
            raise IndexError('Stack is empty')

        return self.__mx


def main():
    stack = Stack()
    write(end="")
    for line in read(type_convert=str):
        if line[0] == 'push':
            stack.push(int(line[1]))
        elif line[0] == 'pop':
            stack.pop()
        elif line[0] == 'max':
            write(stack.max(), to_end=True)
        else:
            raise ValueError('Invalid input')


if __name__ == '__main__':
    main()
