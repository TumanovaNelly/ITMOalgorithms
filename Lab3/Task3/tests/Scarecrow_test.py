import unittest
from random import randint

from Lab3.Task3.src.ScarecrowSort import scarecrow_sort_real_sorting, scarecrow_sort_checking_indexes, main
from utils import time_data, memory_data


class TestScarecrow(unittest.TestCase):
    def test_first_example(self):
        # given
        lst = [2, 1, 3]
        delta = 2
        expected_result = False

        # when
        result_checking_indexes = scarecrow_sort_checking_indexes(lst, delta)
        result_real_sorting = scarecrow_sort_real_sorting(lst, delta)

        # then
        self.assertEqual(result_checking_indexes, expected_result)
        self.assertEqual(result_real_sorting, expected_result)

    def test_second_example(self):
        # given
        lst = [1, 5, 3, 4, 1]
        delta = 3
        expected_result = True

        # when
        result_checking_indexes = scarecrow_sort_checking_indexes(lst, delta)
        result_real_sorting = scarecrow_sort_real_sorting(lst, delta)

        # then
        self.assertEqual(result_checking_indexes, expected_result)
        self.assertEqual(result_real_sorting, expected_result)

    def test_same(self):
        # given
        lst = [1, 1, 1, 1, 1, 1]
        delta = 3
        expected_result = True

        # when
        result_checking_indexes = scarecrow_sort_checking_indexes(lst, delta)
        result_real_sorting = scarecrow_sort_real_sorting(lst, delta)

        # then
        self.assertEqual(result_checking_indexes, expected_result)
        self.assertEqual(result_real_sorting, expected_result)

    def test_simple_delta(self):
        # given
        lst = [randint(0, 1000) for _ in range(1000)]
        delta = 1
        expected_result = True

        # when
        result_checking_indexes = scarecrow_sort_checking_indexes(lst, delta)
        result_real_sorting = scarecrow_sort_real_sorting(lst, delta)

        # then
        self.assertEqual(result_checking_indexes, expected_result)
        self.assertEqual(result_real_sorting, expected_result)

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
