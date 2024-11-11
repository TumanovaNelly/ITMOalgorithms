from typing import List
from Lab3.Task1.src.QuickSort import quick_sort
from Utils.Read_n_Write import read, write


def scarecrow_sort_checking_indexes(lst: List[int], delta: int) -> bool:
    sorted_lst = lst[:]
    quick_sort(sorted_lst)

    value_indexes = dict()
    for index, value in enumerate(lst):
        if value_indexes.get(value) is None:
            value_indexes[value] = []

        value_indexes[value].append(dict(index=index, is_taken=False))


    for index, value in enumerate(sorted_lst):
        for element in value_indexes[value]:
            if not element["is_taken"] and abs(element["index"] - index) % delta == 0:
                element["is_taken"] = True
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


def main():
    delta, lst = read()
    if scarecrow_sort_checking_indexes(lst, *delta):
        write("YES")
    else: write("NO")


if __name__ == "__main__":
    main()
