from typing import TypeVar
from Lab4.Task13.src.List import Node
from utils import read, write

T = TypeVar('T')


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.mid = None
        self.tail = None
        self.__length = 0

    def __len__(self) -> int:
        return self.__length

    def push_back(self, value: T) -> None:
        new_node = Node(value)

        new_node.prev = self.tail
        if new_node.prev is not None:
            new_node.prev.next = new_node
            if self.__length % 2 == 0: self.mid = self.mid.next
        else:
            self.head = self.mid = new_node
        self.tail = new_node

        self.__length += 1

    def push_mid(self, value: T) -> None:
        new_node = Node(value)

        new_node.prev = self.mid
        if self.mid is not None:
            new_node.next = self.mid.next
            self.mid.next = new_node

            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.tail = new_node

            if self.__length % 2 == 0: self.mid = self.mid.next
        else:
            self.head = self.mid = self.tail = new_node

        self.__length += 1

    def pop_front(self) -> T:
        if self.__length == 0:
            raise IndexError('pop index')

        if self.__length % 2 == 0: self.mid = self.mid.next

        pop_node = self.head
        self.head = self.head.next

        self.__length -= 1
        if self.__length == 0:
            self.mid = self.tail = None

        return pop_node.value

    def print(self, end: str = " ") -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=end)
            current_node = current_node.next
        print()


def main():
    queue = Queue()
    write(end="")
    for line in read(type_convert=str):
        if line[0] == '+':
            queue.push_back(line[1])
        elif line[0] == '*':
            queue.push_mid(line[1])
        else:
            write(queue.pop_front(), sep="\n", to_end=True)


if __name__ == '__main__':
    main()
