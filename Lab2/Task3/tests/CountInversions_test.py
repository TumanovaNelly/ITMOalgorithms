from random import shuffle

from Lab2.Task3.src.CountInversions import merge_sort_count_inversions, count_inversions_naive


def test_merge_sort_count_inversions():
    for _ in range(100):
        lst = list(range(1, 1000))
        shuffle(lst)
        assert count_inversions_naive(lst) == merge_sort_count_inversions(lst)
