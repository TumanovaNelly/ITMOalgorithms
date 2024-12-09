import unittest
from random import randint

from utils import time_data, memory_data
from Lab1.Task1.src.InsertionSort import insertion_sort, insertion_sort_bin_pow, main


class TestInsertionSort(unittest.TestCase):
    def test_already_sorted(self):
        # given
        lst1 = [1, 2, 3, 4, 5]
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        # given
        lst1 = [5, 4, 3, 2, 1]
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [1, 2, 3, 4, 5])

    def test_random_order(self):
        # given
        lst1 = [3, 1, 4, 1, 5, 9, 2]
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [1, 1, 2, 3, 4, 5, 9])

    def test_duplicate_elements(self):
        # given
        lst1 = [2, 2, 2, 2, 2]
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [2, 2, 2, 2, 2])

    def test_empty_list(self):
        # given
        lst1 = []
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [])

    def test_single_element(self):
        # given
        lst1 = [42]
        lst2 = lst1[:]

        # when
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)

        # then
        self.assertTrue(lst1 == lst2 == [42])

    def test_random(self):
        for _ in range(100):
            # given
            lst = [randint(-100, 100) for _ in range(randint(0, 100))]
            lst1 = lst[:]
            lst2 = lst[:]
            lst.sort()

            # when
            insertion_sort(lst1)
            insertion_sort_bin_pow(lst2)

            # then
            self.assertTrue(lst1 == lst2 == lst)

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
