import unittest
from random import shuffle

from Lab2.Task3.src.CountInversions import count_inversions_naive, merge_sort_count_inversions, main
from utils import time_data, memory_data


class TestCountInversions(unittest.TestCase):
    def test_merge_sort_count_inversions(self):
        # given
        lst = list(range(1, 1000))
        shuffle(lst)
        inversions_by_naive = count_inversions_naive(lst)

        # when
        inversions = merge_sort_count_inversions(lst)

        # then
        self.assertEqual(inversions_by_naive, inversions)

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 6)
        self.assertLess(peak, 6)


if __name__ == '__main__':
    unittest.main()
