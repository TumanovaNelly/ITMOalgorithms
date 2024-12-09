import unittest
from random import randint

from Lab2.Task7.src.FindMaxSubarray import find_max_subarray, find_max_subarray_naive, main
from utils import time_data, memory_data


class TestFindMaxSubarray(unittest.TestCase):
    def test_find_max_subarray(self):
        for _ in range(100):
            # given
            lst = [randint(-50, 50) for _ in range(100)]
            expected_result = find_max_subarray_naive(lst)

            # when
            result = find_max_subarray(lst)

            # then
            self.assertEqual(result, expected_result)

    def test_find_max_subarray_all_neg(self):
        for _ in range(1000):
            # given
            lst = [randint(-100, 0) for _ in range(100)]
            mx = max(lst)
            ind_mx = lst.index(mx)
            expected_result = (mx, ind_mx, ind_mx + 1)

            # when
            result = find_max_subarray(lst)

            # then
            self.assertEqual(result, expected_result)

    def test_find_max_subarray_all_pos(self):
        for _ in range(1000):
            # given
            lst = [randint(0, 100) for _ in range(100)]
            expected_result = sum(lst)

            # when
            result = find_max_subarray(lst)

            # then
            self.assertEqual(result[0], expected_result)

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
