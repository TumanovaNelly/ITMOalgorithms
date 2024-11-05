from typing import List, Tuple, TypeVar
from random import randint


T = TypeVar("T")


def partition(lst: List[T], start: int, end: int, pivot: T) -> Tuple[int, int]:
    end_left = end_mid = start
    for i in range(start, end):
        if lst[i] < pivot:
            lst[i], lst[end_mid], lst[end_left] = lst[end_mid], lst[end_left], lst[i]
            end_left += 1
            end_mid += 1
        elif lst[i] == pivot:
            lst[end_mid], lst[i] = lst[i], lst[end_mid]
            end_mid += 1

    return end_left, end_mid


def quick_sort(lst: List[T], start: int = 0, end: int = -1) -> None:
    if end == -1:
        end = len(lst)

    if end - start < 2:
        return

    end_left, end_mid = partition(lst, start, end, lst[randint(start,  end - 1)])
    quick_sort(lst, start, end_left)
    quick_sort(lst, end_mid, end)


