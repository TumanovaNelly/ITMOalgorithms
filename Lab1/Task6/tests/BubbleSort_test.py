import unittest
from random import randint

from Lab1.Task6.src.BubbleSort import bubble_sort, main
from utils import time_data, memory_data


class TestBubbleSort(unittest.TestCase):
    def test_already_sorted(self):
        # given
        lst = [1, 2, 3, 4, 5]

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        # given
        lst = [5, 4, 3, 2, 1]

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [1, 2, 3, 4, 5])

    def test_random_order(self):
        # given
        lst = [3, 1, 4, 1, 5, 9, 2]

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [1, 1, 2, 3, 4, 5, 9])

    def test_duplicate_elements(self):
        # given
        lst = [2, 2, 2, 2, 2]

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [2, 2, 2, 2, 2])

    def test_empty_list(self):
        # given
        lst = []

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [])

    def test_single_element(self):
        # given
        lst = [42]

        # when
        bubble_sort(lst)

        # then
        self.assertEqual(lst, [42])

    def test_random(self):
        for _ in range(100):
            # given
            lst = [randint(-100, 100) for _ in range(randint(0, 100))]
            lst_copy = lst[:]
            lst.sort()

            # when
            bubble_sort(lst_copy)

            # then
            self.assertEqual(lst_copy, lst)

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == '__main__':
    unittest.main()
