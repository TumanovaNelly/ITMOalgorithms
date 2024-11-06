from Utils.Read_n_Write import *
from typing import List, Tuple
from random import randint


def get_norma(point: Tuple[int, int]):
    return point[0] ** 2 + point[1] ** 2


def partition_by_norma(lst: List[Tuple[int, int]], start: int, end: int, pivot: Tuple[int, int]) -> Tuple[int, int]:
    end_left = end_mid = start
    pivot_norma = get_norma(pivot)
    for i in range(start, end):
        cur_norma = get_norma(lst[i])
        if cur_norma < pivot_norma:
            lst[i], lst[end_mid], lst[end_left] = lst[end_mid], lst[end_left], lst[i]
            end_left += 1
            end_mid += 1
        elif cur_norma == pivot_norma:
            lst[end_mid], lst[i] = lst[i], lst[end_mid]
            end_mid += 1

    return end_left, end_mid


def quick_sort_by_norma(lst: List[Tuple[int, int]], start: int = 0, end: int = -1) -> None:
    if end == -1:
        end = len(lst)

    if end - start < 2:
        return

    end_left, end_mid = partition_by_norma(lst, start, end, lst[randint(start,  end - 1)])
    quick_sort_by_norma(lst, start, end_left)
    quick_sort_by_norma(lst, end_mid, end)



def nearest_points(lst: List[Tuple[int, int]], number: int):
    quick_sort_by_norma(lst)
    return lst[:number]



def nearest_points_as_quick_sort(lst: List[Tuple[int, int]], number: int, output: List[Tuple[int, int]],
                                 start: int = 0, end: int = -1):
    if end == -1:
        end = len(lst)

    if end - start < 1:
        return

    end_left, end_mid = partition_by_norma(lst, start, end, lst[randint(start, end - 1)])

    if end_left <= number:
        for i in range(end_left):
            output.append(lst[i])

        if end_mid <= number:
            for i in range(end_left, end_mid):
                output.append(lst[i])
            nearest_points_as_quick_sort(lst, number - end_mid, output, end_mid, end)
        else:
            for i in range(end_left, number):
                output.append(lst[i])
            return
    else:
        nearest_points_as_quick_sort(lst, number, output, start, end_left)


def main():
    number, *lst = read()
    answer = []
    nearest_points_as_quick_sort(lst, number, answer)
    write(*answer)


if __name__ == "__main__":
    main()