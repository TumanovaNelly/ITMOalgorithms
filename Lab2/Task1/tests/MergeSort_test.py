import unittest
from random import randint

from Lab2.Task1.src.MergeSort import merge_sort, merge, main
from utils import time_data, memory_data


class TestMergeSort(unittest.TestCase):
    def test_merge(self):
        # given
        merge_result = [0] * 10
        to_merge_lst1, to_merge_lst2 = [1, 2, 3, 4], [1, 4, 6]

        # when
        merge(to_merge_lst1, to_merge_lst2, merge_result, 1)

        # then
        self.assertEqual(merge_result, [0, 1, 1, 2, 3, 4, 4, 6, 0, 0])

    def test_merge_empty(self):
        # given
        merge_result = [0] * 10
        to_merge_lst1, to_merge_lst2 = [], [1, 4, 6]

        # when
        merge(to_merge_lst1, to_merge_lst2, merge_result, 1)

        # then
        self.assertEqual(merge_result, [0, 1, 4, 6, 0, 0, 0, 0, 0, 0])

    def test_merge_sort(self):
        # given
        lst = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 5))]
        lst_sorted = sorted(lst)

        # when
        merge_sort(lst)

        # then
        self.assertEqual(lst, lst_sorted)

    def test_merge_sort_empty(self):
        # given
        lst = []

        # when
        merge_sort(lst)

        # then
        self.assertEqual(lst, [])

    def test_merge_sort_one_elem(self):
        # given
        lst = [100]

        # when
        merge_sort(lst)

        # then
        self.assertEqual(lst, [100])

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 1)
        self.assertLess(peak, 1)


if __name__ == '__main__':
    unittest.main()
