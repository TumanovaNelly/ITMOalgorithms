from typing import Optional, List, Tuple


class Heap:
    def __init__(self, nodes: List[int]) -> None:
        self.__nodes: List[int] = nodes[:]
        self.permutations_to_heap: List[Tuple[int, int]] = []
        self.__heapify()

    def __heapify(self):
        for i in range(len(self.__nodes) - 1, 0, -1):
            self.__sift_up(i)

    def __sift_up(self, element_index: int) -> None:
        while True:
            parent_index: int = self.__get_parent_index(element_index)
            if parent_index is None: return

            if self.__nodes[element_index] < self.__nodes[parent_index]:
                self.__nodes[element_index], self.__nodes[parent_index] = \
                    self.__nodes[parent_index], self.__nodes[element_index]
                self.permutations_to_heap.append((parent_index, element_index))
                element_index = parent_index
            else:
                return

    def __get_parent_index(self, element_index: int) -> Optional[int]:
        return (element_index + 1) // 2 - 1 if element_index > 0 else None


if __name__ == "__main__":
    heap = Heap([5, 4, 3, 2, 1])
    print(*heap.permutations_to_heap, sep="\n")
