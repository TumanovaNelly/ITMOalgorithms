import unittest
from Lab4.Task1.src.Stack import main
from utils import time_data, memory_data


class TestStack(unittest.TestCase):

    def test_time(self):
        self.assertTrue(time_data(main) < 2)

    def test_memory_data(self):
        cur, peak = memory_data(main)
        self.assertTrue(cur < 5)
        self.assertTrue(peak < 5)


if __name__ == "__main__":
    unittest.main()
