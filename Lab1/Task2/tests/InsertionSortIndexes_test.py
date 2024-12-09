import unittest

from utils import time_data, memory_data
from Lab1.Task2.src.InsertionSortIndexes import main


class TestInsertionSortIndexes(unittest.TestCase):
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
