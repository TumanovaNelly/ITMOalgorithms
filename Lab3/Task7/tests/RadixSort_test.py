import unittest

from Lab3.Task7.src.RadixSort import radix_sort, main
from utils import time_data, memory_data


class TestRadixSort(unittest.TestCase):
    def test_radix_sort_first_example(self):
        # given
        lst = ['bab', 'bba', 'baa']
        expected_result = [2, 3, 1]

        # when
        result = radix_sort(lst, 3, 1)

        # then
        self.assertEqual(result, expected_result)

    def test_radix_sort_second_example(self):
        # given
        lst = ['bab', 'bba', 'baa']
        expected_result = [3, 1, 2]

        # when
        result = radix_sort(lst, 3, 2)

        # then
        self.assertEqual(result, expected_result)

    def test_radix_sort_third_example(self):
        # given
        lst = ['bab', 'bba', 'baa']
        expected_result = [3, 1, 2]

        # when
        result = radix_sort(lst, 3, 3)

        # then
        self.assertEqual(result, expected_result)

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
