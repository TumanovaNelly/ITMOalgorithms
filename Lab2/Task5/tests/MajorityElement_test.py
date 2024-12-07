from random import randint
from Lab2.Task5.src.MajorityElement import majority_element_line, majority_element_recursion, main
from utils import time_data, memory_data


def test_majority_elem():
    lst = [2, 3, 9, 2, 2]
    assert majority_element_recursion(lst) == (2, 3) == majority_element_line(lst)


def test_majority_elem_none():
    lst = [1, 2, 3, 4, 5, 6]
    assert majority_element_recursion(lst) == (None, -1) == majority_element_line(lst)


def test_majority_elem_random():
    for _ in range(1000):
        num = 101
        lst = [randint(0, 1) for _ in range(num)]
        zeros = lst.count(0)
        ones = num - zeros

        assert (majority_element_recursion(lst) ==
                (0, zeros) if zeros > ones else (1, ones) ==
                majority_element_line(lst))


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1

