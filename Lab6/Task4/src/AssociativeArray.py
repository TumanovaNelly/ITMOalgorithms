from typing import TypeVar, Callable, Optional, List, Tuple

from utils import read, write
from Lab4.Task13.src.List import Node


KT = TypeVar('KT')
VT = TypeVar('VT')


class AssociativeArray:
    def __init__(self, capacity: int = 100, hash_function: Callable = hash):
        self.__capacity: int = capacity
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.__size: int = 0
        self.__hash_function: Callable = hash_function
        self.__buckets: List[List[Tuple[KT, VT]]] = [[] for _ in range(self.__capacity)]

    def __getitem__(self, key: KT) -> VT:
        item_node = self.__getitem_node(key)
        if item_node is not None:
            return item_node.value
        raise IndexError("Index out of range")

    def get(self, key: KT, if_no_element=None):
        try:
            return self[key]
        except KeyError:
            return if_no_element

    def __getitem_node(self, key: KT) -> Optional[Node]:
        bucket = self.__get_bucket(key)
        for k, v in bucket:
            if k == key: return v
        return None

    def __get_bucket(self, value: VT) -> List[Tuple[KT, VT]]:
        return self.__buckets[self.__hash_function(value) % self.__capacity]

    def previous(self, key: KT) -> Optional[VT]:
        try:
            return self.__getitem_node(key).prev.value
        except AttributeError:
            return None

    def next(self, key: KT) -> Optional[VT]:
        try:
            return self.__getitem_node(key).next.value
        except AttributeError:
            return None

    def __setitem__(self, key: KT, value: VT) -> None:
        bucket = self.__get_bucket(key)
        for k, v in bucket:
            if k == key:
                v.value = value
                return

        value_node = Node(value)
        bucket.append((key, value_node))

        value_node.prev = self.tail
        if value_node.prev is not None:
            value_node.prev.next = value_node
        else:
            self.head = value_node
        self.tail = value_node

        self.__size += 1

    def __delitem__(self, key: KT) -> None:
        bucket = self.__get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                self.__unhook(v)
                del bucket[i]
                self.__size -= 1
                return

        raise KeyError(f"Key {key} not found.")

    def __unhook(self, node: Node) -> VT:
        if node is None:
            raise IndexError("Index out of range")

        if node.next is not None:
            node.next.prev = node.prev
        else: self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        else: self.head = node.next

        return node.value

    def __contains__(self, key: KT) -> bool:
        return any(k == key for k, _ in self.__get_bucket(key))

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        for bucket in self.__buckets:
            for key, _ in bucket:
                yield key


def main():
    array = AssociativeArray()
    write(end="")
    for command, *values in read(type_convert=str):
        if command == "put":
            array[values[0]] = values[1]
        elif command == "get":
            write(array.get(values[0]), to_end=True)
        elif command == "prev":
            write(array.previous(values[0]), to_end=True)
        elif command == "next":
            write(array.next(values[0]), to_end=True)
        elif command == "delete":
            del array[values[0]]
        else: raise ValueError("Unknown command")

if __name__ == "__main__":
    main()



