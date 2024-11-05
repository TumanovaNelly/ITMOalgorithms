from Lab3.Task5.src.Hirsch import hirsch
from Utils.Time_Memory import time_data
from Lab3.Task5.src.main import main


def test_hirsch_first_example():
    lst = [3, 0, 6, 1, 5]
    assert hirsch(lst) == 3


def test_hirsch_second_example():
    lst = [1, 3, 1]
    assert hirsch(lst) == 1


def test_time():
    time = time_data(main)
    assert time < 2




