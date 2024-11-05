from typing import List
from Lab3.Task1.src.QuickSort import quick_sort


def scarecrow_sort_checking_indexes(lst: List[int], delta: int) -> bool:
    sorted_lst = lst[:]
    quick_sort(sorted_lst)

    is_taken = [False for _ in range(len(lst))]
    for index, value in enumerate(sorted_lst):
        for i in range(index % delta, len(lst), delta):
            if lst[i] == value and not is_taken[i]:
                is_taken[i] = True
                break
        else: return False

    return True


def scarecrow_sort_real_sorting(lst: List[int], delta: int) -> bool:
    sorted_lst = lst[:]
    quick_sort(sorted_lst)

    for i in range(delta, len(lst)):
        cur = i
        while cur > 0 and lst[cur - delta] > lst[cur]:
            lst[cur - delta], lst[cur] = lst[cur], lst[cur - delta]
            cur -= 1

    return sorted_lst == lst

