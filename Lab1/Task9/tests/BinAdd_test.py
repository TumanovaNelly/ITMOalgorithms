import unittest

from Lab1.Task9.src.BinAdd import bin_add, main
from utils import time_data, memory_data


class TestBinAdd(unittest.TestCase):
    def test_bin_add_same_length(self):
        # given
        first, second = [1, 0, 1], [1, 1, 0]
        first_plus_second = [1, 0, 1, 1]

        # when
        bin_add_result = bin_add(first, second)

        # then
        self.assertEqual(bin_add_result, first_plus_second)

    def test_bin_add_different_length(self):
        # given
        first, second = [1, 0], [1, 1, 1]
        first_plus_second = [1, 0, 0, 1]

        # when
        bin_add_result = bin_add(first, second)

        # then
        self.assertEqual(bin_add_result, first_plus_second)

    def test_bin_add_all_zeros(self):
        # given
        first, second = [0, 0, 0], [0, 0, 0]
        first_plus_second = [0, 0, 0, 0]

        # when
        bin_add_result = bin_add(first, second)

        # then
        self.assertEqual(bin_add_result, first_plus_second)

    def test_bin_add_one_bit(self):
        # given
        first, second = [1], [1]
        first_plus_second = [1, 0]

        # when
        bin_add_result = bin_add(first, second)

        # then
        self.assertEqual(bin_add_result, first_plus_second)

    def test_bin_add_large_numbers(self):
        # given
        first, second = [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]
        first_plus_second = [1, 1, 1, 1, 1, 0]

        # when
        bin_add_result = bin_add(first, second)

        # then
        self.assertEqual(bin_add_result, first_plus_second)

    def test_bin_add_invalid_input(self):
        # (then, when, *given)
        self.assertRaises(ValueError, bin_add, [1, 0, 2], [0, 1, 0])

    def test_bin_add_invalid_input_non_binary(self):
        # (then, when, *given)
        self.assertRaises(ValueError, bin_add, [1, 0, 1], [1, 0, 5])

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
