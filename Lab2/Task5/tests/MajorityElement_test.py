import unittest
from random import randint

from Lab2.Task5.src.MajorityElement import majority_element_line, majority_element_recursion, main
from utils import time_data, memory_data


class TestMajorityElement(unittest.TestCase):
    def test_majority_elem(self):
        # given
        lst = [2, 3, 9, 2, 2]
        expected_result = (2, 3)

        # when
        result_recursion = majority_element_recursion(lst)
        result_line = majority_element_line(lst)

        # then
        self.assertEqual(result_recursion, expected_result)
        self.assertEqual(result_line, expected_result)

    def test_majority_elem_none(self):
        # given
        lst = [1, 2, 3, 4, 5, 6]
        expected_result = (None, -1)

        # when
        result_recursion = majority_element_recursion(lst)
        result_line = majority_element_line(lst)

        # then
        self.assertEqual(result_recursion, expected_result)
        self.assertEqual(result_line, expected_result)

    def test_majority_elem_random(self):
        for _ in range(1000):
            # given
            elements_number = 101
            lst = [randint(0, 1) for _ in range(elements_number)]
            zeros = lst.count(0)
            ones = elements_number - zeros
            expected_result = (0, zeros) if zeros > ones else (1, ones)

            # when
            result_recursion = majority_element_recursion(lst)
            result_line = majority_element_line(lst)

            # then
            self.assertEqual(result_recursion, expected_result)
            self.assertEqual(result_line, expected_result)

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
