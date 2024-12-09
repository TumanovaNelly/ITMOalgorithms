import unittest
from random import randint

from Lab3.Task1.src.QuickSort import partition, quick_sort, main
from utils import time_data, memory_data


class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        # given
        lst = [randint(1, 100) for _ in range(100)]
        pivot = randint(1, 100)
        left_part = [el for el in lst if el < pivot]
        mid_part = [el for el in lst if el == pivot]

        # when
        end_left_part, end_mid_part = partition(lst, 0, len(lst), pivot)

        # then
        self.assertEqual(end_left_part, len(left_part))
        self.assertEqual(end_mid_part, len(left_part) + len(mid_part))
        self.assertEqual(left_part, lst[:end_left_part])

    def test_quick_sort_random_int(self):
        # given
        lst = [randint(-100, 100) for _ in range(1000)]
        lst_sorted = sorted(lst)

        # when
        quick_sort(lst)

        # then
        self.assertEqual(lst, lst_sorted)

    def test_quick_sort_random_str(self):
        # given
        lst = [str(randint(10, 100)) for _ in range(1000)]
        lst_sorted = sorted(lst)

        # when
        quick_sort(lst)

        # then
        self.assertEqual(lst, lst_sorted)

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
