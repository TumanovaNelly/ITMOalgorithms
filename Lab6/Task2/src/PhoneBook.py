from optparse import Values
from typing import Callable, TypeVar, List, Tuple

from utils import read, write


VT = TypeVar('VT')
KT = TypeVar('KT')


class CustomDict:
    def __init__(self, capacity: int = 100, hash_function: Callable = hash):
        self.__capacity: int = capacity
        self.__size: int = 0
        self.__hash_function: Callable = hash_function
        self.__buckets: List[List[Tuple[KT, VT]]] = [[] for _ in range(self.__capacity)]

    def get(self, key: KT, if_no_element = None) -> VT:
        try:
            return self[key]
        except KeyError:
            return if_no_element

    def __getitem__(self, key: KT) -> VT:
        bucket = self.__get_bucket(key)
        for k, v in bucket:
            if k == key: return v

        raise KeyError(f"Key {key} not found")

    def __get_bucket(self, value: VT) -> List[Tuple[KT, VT]]:
        return self.__buckets[self.__hash_function(value) % self.__capacity]

    def __setitem__(self, key: KT, value: VT) -> None:
        bucket = self.__get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.__size += 1

    def __delitem__(self, key: KT) -> None:
        bucket = self.__get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.__size -= 1
                return

        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key: KT) -> bool:
        return any(k == key for k, _ in self.__get_bucket(key))

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        for bucket in self.__buckets:
            for key, _ in bucket:
                yield key




if __name__ == "__main__":
    custom_dict = CustomDict()

    write(end="")
    for command, *values in read(type_convert=str):
        if command == "add":
            custom_dict[values[0]] = values[1]
        elif command == "del":
            try:
                del custom_dict[values[0]]
            except KeyError: pass
        elif command == "find":
            write(custom_dict.get(values[0], "not found"), to_end=True)
        else: raise ValueError(f"Unknown command: {command}")