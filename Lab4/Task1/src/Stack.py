from typing import TypeVar
from Lab4.Task13.src.SingleLinkedList import SingleLinkedList
from Utils.Read_n_Write import read, write

T = TypeVar('T')


class Stack:
    def __init__(self):
        self.stack = SingleLinkedList()

    def push(self, item: T) -> None:
        self.stack.push(item)

    def pop(self) -> T:
        return self.stack.pop()


def main():
    stack = Stack()
    write()
    for line in read(type_convert=str):
        if line[0] == '+':
            stack.push(line[1])
        else: write(stack.pop(), sep="\n", to_end=True)


if __name__ == '__main__':
    main()
