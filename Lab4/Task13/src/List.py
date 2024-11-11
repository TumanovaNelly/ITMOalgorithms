from typing import TypeVar, Union

T = TypeVar('T')

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class List:
    def __init__(self) -> None:
        self.head: T = None
        self.tail: T = None
        self.length = 0


    def push_back(self, value: T) -> None:
        new_value = Node(value)
        if self.length > 0:
            self.tail.next = new_value
        else: self.head = new_value

        new_value.prev = self.tail

        self.tail = new_value
        self.length += 1


    def push_front(self, value: T) -> None:
        new_value = Node(value)
        if self.length > 0:
            self.head.prev = new_value
        else: self.tail = new_value

        new_value.next = self.head

        self.head = new_value
        self.length += 1


    def pop_back(self) -> T:
        if self.length == 0:
            raise IndexError('pop index')

        pop_node = self.tail
        self.tail = self.tail.prev
        self.length -= 1
        return pop_node.value


    def pop_front(self) -> T:
        if self.length == 0:
            raise IndexError('pop index')

        pop_node = self.head
        self.head = self.head.next
        self.length -= 1
        return pop_node.value


    def find(self, value: T) -> Node:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        raise ValueError('value not found')


    def remove_after(self, value: T) -> T:
        return self.remove(self.find(value).next)


    def remove_before(self, value: T) -> T:
        return self.remove(self.find(value).prev)


    def remove(self, node: Node) -> T:
        if node is None:
            raise IndexError('List index out of range')

        if node.next is not None:
            node.next.prev = node.prev
        else: self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        else: self.head = node.next

        self.length -= 1
        return node.value


    def print(self, end: str = " ") -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=end)
            current_node = current_node.next


if __name__ == '__main__':
    pass