import unittest

from Lab3.Task5.src.Hirsch import hirsch, main
from utils import time_data, memory_data


class TestHirsch(unittest.TestCase):
    def test_hirsch_first_example(self):
        # given
        lst = [3, 0, 6, 1, 5]
        expected_result = 3

        # when
        result = hirsch(lst)

        # then
        self.assertEqual(result, expected_result)

    def test_hirsch_second_example(self):
        # given
        lst = [1, 3, 1]
        expected_result = 1

        # when
        result = hirsch(lst)

        # then
        self.assertEqual(result, expected_result)

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
