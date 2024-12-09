import unittest

from utils import time_data, memory_data
from Lab1.Task7.src.BubbleSortIndexes import main


class TestBubbleSortIndexes(unittest.TestCase):
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
