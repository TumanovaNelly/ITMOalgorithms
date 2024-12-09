from typing import List, Tuple

from utils import read, write


class Heap:
    def __init__(self, nodes: List[int]) -> None:
        self.__nodes: List[int] = nodes[:]
        self.permutations_to_heap: List[Tuple[int, int]] = []
        self.__heapify()

    def __heapify(self):
        for i in range(len(self.__nodes) - 1, -1, -1):
            self.__sift_down(i)

    def __sift_down(self, element_index: int) -> None:
        while True:
            left_child_index: int = self.__get_left_child_index(element_index)
            if left_child_index is None: return
            right_child_index: int = self.__get_right_child_index(element_index)

            min_child_index = left_child_index \
                if (right_child_index is None or
                    self.__nodes[left_child_index] < self.__nodes[right_child_index]) \
                else right_child_index

            if self.__nodes[min_child_index] < self.__nodes[element_index]:
                self.__nodes[element_index], self.__nodes[min_child_index] = \
                    self.__nodes[min_child_index], self.__nodes[element_index]
                self.permutations_to_heap.append((element_index, min_child_index))
                element_index = min_child_index
            else:
                return

    def __get_left_child_index(self, element_index: int) -> int:
        child_index = element_index * 2 + 1
        return child_index if child_index < len(self.__nodes) else None

    def __get_right_child_index(self, element_index: int) -> int:
        child_index = element_index * 2 + 2
        return child_index if child_index < len(self.__nodes) else None


def main():
    data, = read()
    write(*Heap(data).permutations_to_heap, sep="\n")


if __name__ == "__main__":
    main()
