from typing import List, Optional

from utils import read, write


def find_last_less(value, data_list: List[float]) -> int:
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return right


def increasing_subarray(array: List[int]):
    data_list = [float('inf')] * (len(array) + 1)
    data_list[0] = float('-inf')
    position: List[Optional[int]] = [None] * (len(array) + 1)
    previous: List[Optional[int]] = [None] * len(array)

    length: int = 0
    for index, item in enumerate(array):
        last_less = find_last_less(item, data_list)
        after_last_less = last_less + 1
        if item < data_list[after_last_less]:
            data_list[after_last_less] = item
            position[after_last_less] = index
            previous[index] = position[last_less]
        length = max(length, after_last_less)

    subarray = []
    current_index = position[length]
    while current_index is not None:
        subarray.append(array[current_index])
        current_index = previous[current_index]

    return reversed(subarray)


def main():
    array, = read()
    write(*increasing_subarray(array))


if __name__ == "__main__":
    main()
