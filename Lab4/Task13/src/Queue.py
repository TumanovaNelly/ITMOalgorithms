from typing import TypeVar
from Lab4.Task13.src.List import List

T = TypeVar('T')


class Queue:
    def __init__(self):
        self.queue = List()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def push(self, item: T) -> None:
        self.queue.push_back(item)

    def pop(self) -> T:
        return self.queue.pop_front()
