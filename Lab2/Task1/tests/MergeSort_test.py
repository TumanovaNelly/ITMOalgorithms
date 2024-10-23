from random import randint

from Lab2.Task1.src.MergeSort import merge, merge_sort


def test_merge():
    lst = [0] * 10
    merge([1, 2, 3, 4], [1, 4, 6], lst, 1)
    assert lst == [0, 1, 1, 2, 3, 4, 4, 6, 0, 0]

def test_merge_empty():
    lst = [0] * 10
    merge([], [1, 4, 6], lst, 1)
    assert lst == [0, 1, 4, 6, 0, 0, 0, 0, 0, 0]

def test_merge_sort():
    lst = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 5))]
    lst_copy = lst[:]
    merge_sort(lst)
    assert lst == sorted(lst_copy)

def test_merge_sort_empty():
    lst = []
    merge_sort(lst)
    assert lst == []

def test_merge_sort_one_elem():
    lst = [100]
    merge_sort(lst)
    assert lst == [100]