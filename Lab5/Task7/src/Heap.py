from typing import TypeVar, Optional, List


class SupportsLT:
    def __lt__(self, other) -> bool: ...


Comparable = TypeVar('Comparable', bound=SupportsLT)


class Heap:
    def __init__(self, is_reversed: bool = False):
        self.__nodes: List[Comparable] = []
        self.__is_reversed = is_reversed

    def add(self, element: Comparable) -> None:
        self.__nodes.append(element)
        self.__sift_up(len(self.__nodes) - 1)

    def extract_min(self) -> Comparable:
        if len(self.__nodes) == 1: return self.__nodes.pop()
        min_value = self.__nodes[0]
        self.__nodes[0] = self.__nodes.pop()
        self.__sift_down(0)
        return min_value

    def __sift_up(self, element_index: int) -> None:
        while True:
            parent_index: int = self.__get_parent_index(element_index)
            if parent_index is None: return

            if (self.__nodes[element_index] < self.__nodes[parent_index]) != self.__is_reversed:
                self.__nodes[element_index], self.__nodes[parent_index] = \
                    self.__nodes[parent_index], self.__nodes[element_index]
                element_index = parent_index
            else: return

    def __sift_down(self, element_index: int) -> None:
        while True:
            left_child_index: int = self.__get_left_child_index(element_index)
            if left_child_index is None: return
            right_child_index: int = self.__get_right_child_index(element_index)

            min_child_index = left_child_index \
                if (right_child_index is None or
                    (self.__nodes[left_child_index] < self.__nodes[right_child_index]) != self.__is_reversed) \
                else right_child_index

            if (self.__nodes[min_child_index] < self.__nodes[element_index]) != self.__is_reversed:
                self.__nodes[element_index], self.__nodes[min_child_index] = \
                    self.__nodes[min_child_index], self.__nodes[element_index]
                element_index = min_child_index
            else: return

    def __get_parent_index(self, element_index: int) -> Optional[int]:
        return (element_index + 1) // 2 - 1 if element_index > 0 else None

    def __get_left_child_index(self, element_index: int) -> int:
        child_index = element_index * 2 + 1
        return child_index if child_index < len(self.__nodes) else None

    def __get_right_child_index(self, element_index: int) -> int:
        child_index = element_index * 2 + 2
        return child_index if child_index < len(self.__nodes) else None


if __name__ == "__main__":
    heap = Heap(is_reversed=True)
