from random import randint
from Lab3.Task3.src.ScarecrowSort import scarecrow_sort_real_sorting, scarecrow_sort_checking_indexes, main
from utils import time_data, memory_data



def test_first_example():
    lst = [2, 1, 3]
    delta = 2
    assert (scarecrow_sort_checking_indexes(lst, delta) ==
            scarecrow_sort_real_sorting(lst, delta) ==
            False)


def test_second_example():
    lst = [1, 5, 3, 4, 1]
    delta = 3
    assert (scarecrow_sort_checking_indexes(lst, delta) ==
            scarecrow_sort_real_sorting(lst, delta) ==
            True)


def test_same():
    lst = [1, 1, 1, 1, 1, 1]
    delta = 3
    assert (scarecrow_sort_checking_indexes(lst, delta) ==
            scarecrow_sort_real_sorting(lst, delta) ==
            True)


def test_simple_delta():
    lst = [randint(0, 1000) for _ in range(1000)]
    delta = 1
    assert (scarecrow_sort_checking_indexes(lst, delta) ==
            scarecrow_sort_real_sorting(lst, delta) ==
            True)


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 5
    assert peak < 5
