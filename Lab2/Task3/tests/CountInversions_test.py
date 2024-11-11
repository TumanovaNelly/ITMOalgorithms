from random import shuffle

from Lab2.Task3.src.CountInversions import count_inversions_naive, merge_sort_count_inversions, main
from utils import time_data, memory_data


def test_merge_sort_count_inversions():
    for _ in range(100):
        lst = list(range(1, 1000))
        shuffle(lst)
        assert count_inversions_naive(lst) == merge_sort_count_inversions(lst)


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1