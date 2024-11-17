from typing import TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, value) -> None:
        self.value: T = value
        self.next = None
        self.prev = None


class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__length = 0

    def __len__(self) -> int:
        return self.__length

    def push_back(self, value: T) -> None:
        new_node = Node(value)

        new_node.prev = self.tail
        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

        self.__length += 1

    def push_front(self, value: T) -> None:
        new_node = Node(value)

        new_node.next = self.head
        if new_node.next is not None:
            new_node.next.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

        self.__length += 1

    def pop_back(self) -> T:
        if self.__length == 0:
            raise IndexError('pop index')

        pop_node = self.tail
        self.tail = self.tail.prev
        self.__length -= 1
        return pop_node.value

    def pop_front(self) -> T:
        if self.__length == 0:
            raise IndexError('pop index')

        pop_node = self.head
        self.head = self.head.next
        self.__length -= 1
        return pop_node.value

    def find(self, value: T) -> Node:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        raise ValueError('value not found')

    def remove_after(self, value: T) -> T:
        return self.__remove(self.find(value).next)

    def remove_before(self, value: T) -> T:
        return self.__remove(self.find(value).prev)

    def __remove(self, node: Node) -> T:
        if node is None:
            raise IndexError('List index out of range')

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        self.__length -= 1
        return node.value

    def print(self, sep: str = " ") -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=sep)
            current_node = current_node.next
        print()


if __name__ == '__main__':
    pass
