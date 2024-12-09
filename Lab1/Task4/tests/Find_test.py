import unittest

from utils import time_data, memory_data
from Lab1.Task4.src.Find import find, main


class TestFind(unittest.TestCase):
    def test_find_found(self):
        # given
        lst = [1, 2, 3, 4, 5]
        value = 3

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [3])

    def test_find_not_found(self):
        # given
        lst = [1, 2, 3, 4, 5]
        value = 6

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [-1])

    def test_find_first_element(self):
        # given
        lst = [1, 2, 3, 4, 5]
        value = 1

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [1])

    def test_find_last_element(self):
        # given
        lst = [1, 2, 3, 4, 5]
        value = 5

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [5])

    def test_find_empty_list(self):
        # given
        lst = []
        value = 1

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [-1])

    def test_find_multiple_occurrences(self):
        # given
        lst = [1, 2, 3, 2, 5]
        value = 2

        # when
        find_indexes = find(lst, value)

        # then
        self.assertEqual(find_indexes, [2, 4])

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
