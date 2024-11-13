from random import randint

from Lab3.Task1.src.QuickSort import partition, quick_sort, main
from utils import time_data, memory_data


def test_partition():
    # given
    lst = [randint(1, 100) for _ in range(100)]
    pivot = randint(1, 100)

    # when
    left = [el for el in lst if el < pivot]
    mid = [el for el in lst if el == pivot]

    end_left, end_mid = partition(lst, 0, len(lst), pivot)
    # then
    assert end_left == len(left) and end_mid == len(left) + len(mid)
    assert left == lst[:end_left]


def test_quick_sort_random_int():
    # given
    lst = [randint(-100, 100) for _ in range(1000)]
    lst_sorted = sorted(lst)
    # when
    quick_sort(lst)
    # then
    assert lst == lst_sorted


def test_quick_sort_random_str():
    # given
    lst = [str(randint(10, 100)) for _ in range(1000)]
    # when
    lst_sorted = sorted(lst)
    quick_sort(lst)
    # then
    assert lst == lst_sorted


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1

