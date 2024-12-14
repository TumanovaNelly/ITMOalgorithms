from typing import TypeVar, Callable, Optional, List, Tuple

from utils import read, write

KT = TypeVar('KT')
VT = TypeVar('VT')


class DictNode:
    def __init__(self, key: KT, value: VT) -> None:
        self.key: KT = key
        self.value: VT = value
        self.next = None
        self.prev = None

class AssociativeArray:
    def __init__(self, capacity: int = 100, hash_function: Callable = hash):
        self.__capacity: int = capacity
        self.head: Optional[DictNode] = None
        self.tail: Optional[DictNode] = None
        self.__size: int = 0
        self.__hash_function: Callable = hash_function
        self.__buckets: List[List[DictNode]] = [[] for _ in range(self.__capacity)]

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

    def __getitem_node(self, key: KT) -> Optional[DictNode]:
        bucket = self.__get_bucket(key)
        for node in bucket:
            if node.key == key: return node
        return None

    def __get_bucket(self, key: VT) -> List[DictNode]:
        return self.__buckets[self.__hash_function(key) % self.__capacity]

    def previous(self, key: KT) -> Optional[KT]:
        try:
            return self.__getitem_node(key).prev.key
        except AttributeError:
            return None

    def next(self, key: KT) -> Optional[KT]:
        try:
            return self.__getitem_node(key).next.key
        except AttributeError:
            return None

    def __setitem__(self, key: KT, value: VT) -> None:
        bucket = self.__get_bucket(key)
        for i, node in enumerate(bucket):
            if node.key == key:
                self.__unhook(node)
                del bucket[i]
                self.__size -= 1

        value_node = DictNode(key, value)
        bucket.append(value_node)

        value_node.prev = self.tail
        if value_node.prev is not None:
            value_node.prev.next = value_node
        else:
            self.head = value_node
        self.tail = value_node

        self.__size += 1

    def __delitem__(self, key: KT) -> None:
        bucket = self.__get_bucket(key)
        for i, node in enumerate(bucket):
            if node.key == key:
                self.__unhook(node)
                del bucket[i]
                self.__size -= 1
                return

        raise KeyError(f"Key {key} not found.")

    def __unhook(self, node: DictNode) -> VT:
        if node is None:
            raise IndexError("Index out of range")

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        return node.value

    def __contains__(self, key: KT) -> bool:
        return any(node.key == key for node in self.__get_bucket(key))

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.key
            node = node.next


def main():
    array = AssociativeArray()
    write(end="")
    for command, *values in read(type_convert=str):
        if command == "put":
            array[values[0]] = values[1]
        elif command == "get":
            write(array.get(values[0]), to_end=True)
        elif command == "prev":
            prev_key = array.previous(values[0])
            write(array[prev_key] if prev_key is not None else "<none>", to_end=True)
        elif command == "next":
            next_key = array.next(values[0])
            write(array[next_key] if next_key is not None else "<none>", to_end=True)
        elif command == "delete":
            del array[values[0]]
        else:
            raise ValueError("Unknown command")


if __name__ == "__main__":
    main()
