import unittest

from Lab7.Task6.src.IncreasingSubarray import main, increasing_subarray
from utils import time_data, memory_data


class TestIncreasingSubarray(unittest.TestCase):
    def test_increasing_subarray(self):
        # given
        data = [([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
                ([5, 4, 3, 2, 1], [1]),
                ([3, 23, 5, 5, 34, 6], [3, 5, 6])]

        for input, expected in data:
            result = list(increasing_subarray(input))
            self.assertEqual(result, expected)

    def test_time(self):
        # when
        time = time_data(main)
        # then
        self.assertLess(time, 1)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)
        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == "__main__":
    unittest.main()
