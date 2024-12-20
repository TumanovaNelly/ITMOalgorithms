import typing as tp
from utils import read, write


def bin_pow(lst: tp.List[int], value: int) -> int:
    lst_indexes = list(range(len(lst)))
    lst_indexes.sort(key=lambda index: lst[index]) # индексы элементов отсортированного списка lst

    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[lst_indexes[mid]] == value:
            return lst_indexes[mid]
        if lst[lst_indexes[mid]] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1



def main():
    lst, (value, ) = read()
    write(bin_pow(lst, value))


if __name__ == "__main__":
    main()
