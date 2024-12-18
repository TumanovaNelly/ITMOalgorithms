import unittest
from Lab4.Task1.src.Stack import main
from utils import time_data, memory_data


class TestStack(unittest.TestCase):
    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 5)
        self.assertLess(peak, 5)


if __name__ == "__main__":
    unittest.main()