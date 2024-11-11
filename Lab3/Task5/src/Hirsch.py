from typing import List

from Lab3.Task1.src.QuickSort import quick_sort
from utils import read, write


def hirsch(lst: List[int]):
    quick_sort(lst)

    for i in range(len(lst)):
        if len(lst) - i <= lst[i] != lst[i - 1]:
            return len(lst) - i

    return 0


def main():
    lst, = read()
    write(hirsch(lst))


if __name__ == "__main__":
    main()