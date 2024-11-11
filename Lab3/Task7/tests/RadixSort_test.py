from Lab3.Task7.src.RadixSort import radix_sort, main
from utils import time_data, memory_data


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
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 5
    assert peak < 5

