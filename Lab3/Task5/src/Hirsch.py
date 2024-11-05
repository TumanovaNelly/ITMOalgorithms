from typing import List
from Lab3.Task1.src.QuickSort import quick_sort


def hirsch(lst: List[int]):
    quick_sort(lst)

    for i in range(len(lst)):
        if lst[i] >= len(lst) - i:
            return len(lst) - i

    return 0