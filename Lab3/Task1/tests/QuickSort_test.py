from random import randint
from Lab3.Task1.src.QuickSort import partition, quick_sort
from Utils.Time_Memory import time_data
from Lab3.Task1.src.main import main


def test_partition():
    lst = [randint(1, 100) for _ in range(100)]
    pivot = randint(1, 100)

    left = [el for el in lst if el < pivot]
    mid = [el for el in lst if el == pivot]

    end_left, end_mid = partition(lst, 0, len(lst), pivot)
    assert end_left == len(left) and end_mid == len(left) + len(mid)
    assert left == lst[:end_left]


def test_quick_sort_random_int():
    lst = [randint(-100, 100) for _ in range(1000)]
    lst_sorted = sorted(lst)
    quick_sort(lst, 0, len(lst))
    assert lst == lst_sorted


def test_quick_sort_random_str():
    lst = [str(randint(10, 100)) for _ in range(1000)]
    lst_sorted = sorted(lst)
    quick_sort(lst, 0, len(lst))
    assert lst == lst_sorted


def test_time():
    time = time_data(main)
    assert time < 2

