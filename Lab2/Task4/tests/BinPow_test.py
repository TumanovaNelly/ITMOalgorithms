import unittest
from random import randint

from Lab2.Task4.src.BinPow import bin_pow, main
from utils import time_data, memory_data


class TestBinPow(unittest.TestCase):
    def test_bin_pow(self):
        for _ in range(1000):
            # given
            lst = [randint(-100, 100) for _ in range(1000)]
            lst.sort()
            value = randint(-100, 100)

            # when
            index = bin_pow(lst, value)

            # then
            if index == -1: self.assertNotIn(value, lst)
            else: self.assertEqual(lst[index], value)

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
