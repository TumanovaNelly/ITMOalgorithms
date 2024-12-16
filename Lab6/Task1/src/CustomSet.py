from typing import Callable, List, TypeVar

from utils import read, write

T = TypeVar('T')


class CustomSet:
    def __init__(self, capacity: int = 100, hash_function: Callable = hash):
        self.__capacity: int = capacity
        self.__size: int = 0
        self.__hash_function: Callable = hash_function
        self.__buckets: List[List[T]] = [[] for _ in range(self.__capacity)]

    def add(self, value: T) -> None:
        bucket = self.__get_bucket(value)
        if value not in bucket:
            bucket.append(value)
            self.__size += 1

    def remove(self, value: T) -> None:
        bucket = self.__get_bucket(value)
        if value in bucket:
            bucket.remove(value)
            self.__size -= 1
        else:
            raise KeyError(f"Element {value} not found in set.")

    def __contains__(self, value: T) -> bool:
        return value in self.__get_bucket(value)

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        for bucket in self.__buckets:
            for value in bucket:
                yield value

    def __get_bucket(self, value: T) -> List[T]:
        return self.__buckets[self.__hash_function(value) % self.__capacity]


def main():
    custom_set = CustomSet()
    write(end="")
    for command, value in read(type_convert=str):
        if command == "A":
            custom_set.add(value)
        elif command == "D":
            custom_set.remove(value)
        elif command == "?":
            write("YES" if value in custom_set else "NO", to_end=True)
        else:
            raise ValueError(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
