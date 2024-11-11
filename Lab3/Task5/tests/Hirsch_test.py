from Lab3.Task5.src.Hirsch import hirsch, main
from utils import time_data, memory_data


def test_hirsch_first_example():
    lst = [3, 0, 6, 1, 5]
    assert hirsch(lst) == 3


def test_hirsch_second_example():
    lst = [1, 3, 1]
    assert hirsch(lst) == 1


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 5
    assert peak < 5




