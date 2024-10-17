from random import randint
from Lab2.Task7.src.FindMaxSubarray import find_max_subarray, find_max_subarray_naive

def test_find_max_subarray():
    for _ in range(100):
        lst = [randint(-50, 50) for _ in range(100)]
        assert find_max_subarray_naive(lst) == find_max_subarray(lst)


def test_find_max_subarray_all_neg():
    lst = [randint(-100, 0) for _ in range(100)]
    assert find_max_subarray_naive(lst) == find_max_subarray(lst)


def test_find_max_subarray_all_pos():
    lst = [randint(0, 100) for _ in range(100)]
    assert find_max_subarray_naive(lst) == find_max_subarray(lst)