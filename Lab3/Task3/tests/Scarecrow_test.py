from random import randint
from Lab3.Task3.src.ScarecrowSort import *
from Utils.Time_Memory import time_data



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
    lst = [randint(0, 1000) for _ in range(10000)]
    delta = 1
    assert (scarecrow_sort_checking_indexes(lst, delta) ==
            scarecrow_sort_real_sorting(lst, delta) ==
            True)


def test_time():
    time = time_data(main)
    assert time < 2
