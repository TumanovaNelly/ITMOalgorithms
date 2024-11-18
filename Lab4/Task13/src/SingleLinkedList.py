from typing import TypeVar, Union

T = TypeVar('T')


class SingleLinkedNode:
    def __init__(self, value) -> None:
        self.value: T = value
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.__length = 0

    def __len__(self) -> int:
        return self.__length

    def push(self, value: T) -> None:
        new_node = SingleLinkedNode(value)

        new_node.next = self.head
        self.head = new_node

        self.__length += 1

    def pop(self) -> T:
        if self.__length == 0:
            raise IndexError('pop index')

        pop_node = self.head
        self.head = self.head.next

        self.__length -= 1
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
        self.__length -= 1
        return removed_node.value

    def print(self, sep: str = " ") -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=sep)
            current_node = current_node.next
        print()


