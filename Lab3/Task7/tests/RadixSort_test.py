from Lab3.Task7.src.RadixSort import *
from Utils.Time_Memory import time_data


def test_radix_sort_first_example():
    lst = ['bab', 'bba', 'baa']
    assert radix_sort(lst, 3, 1) == [2, 3, 1]


def test_radix_sort_second_example():
    lst = ['bab', 'bba', 'baa']
    assert radix_sort(lst, 3, 2) == [3, 1, 2]


def test_radix_sort_third_example():
    lst = ['bab', 'bba', 'baa']
    assert radix_sort(lst, 3, 3) == [3, 1, 2]


def test_time():
    time = time_data(main)
    assert time < 3

