import unittest

from Lab5.Task1.src.CheckHeap import check_heap, main
from utils import time_data, memory_data


class CheckHeap(unittest.TestCase):
    def test_simple_data(self):
        # given
        expressions = [
            [1, 0, 1, 2, 0],
            [1, 3, 2, 5, 4]
        ]
        expected_results = [False, True]

        for index, expression in enumerate(expressions):
            # when
            result = check_heap(expression)

            # then
            self.assertEqual(result, expected_results[index])

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
