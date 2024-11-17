from typing import TypeVar
from Lab4.Task13.src.SingleLinkedList import SingleLinkedList

T = TypeVar('T')


class Stack:
    def __init__(self):
        self.stack = SingleLinkedList()

    def is_empty(self) -> int:
        return len(self.stack) == 0

    def push(self, item: T) -> None:
        self.stack.push(item)

    def pop(self) -> T:
        return self.stack.pop()
