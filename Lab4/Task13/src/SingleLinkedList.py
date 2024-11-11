from typing import TypeVar, Union

T = TypeVar('T')

class SingleLinkedNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: T = None
        self.length = 0


    def push(self, value: T) -> None:
        new_value = SingleLinkedNode(value)
        new_value.next = self.head
        self.head = new_value
        self.length += 1


    def pop(self) -> T:
        if self.length == 0:
            raise IndexError('pop index')

        pop_node = self.head
        self.head = self.head.next
        self.length -= 1
        return pop_node.value


    def find(self, value: T) -> Union[SingleLinkedNode, None]:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        raise ValueError('Value not found')


    def remove_after(self, value: T) -> T:
        current_node = self.find(value)
        if current_node.next is None:
            raise IndexError('Index out of range')

        removed_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        return removed_node.value


    def print(self, end: str = " ") -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=end)
            current_node = current_node.next


if __name__ == '__main__':
    pass