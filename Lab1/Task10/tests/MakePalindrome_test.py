import unittest

from utils import time_data, memory_data
from Lab1.Task10.src.MakePalindrome import make_palindrome, make_palindrome_general, main


class TestMakePalindrome(unittest.TestCase):
    def test_make_palindrome_even_count(self):
        # given
        input_data = "BABACC"
        expected_output = "ABCCBA"

        input_data_for_general = "babacc"
        expected_output_for_general = "abccba"

        # when
        result_palindrome = make_palindrome(input_data)
        result_general_palindrome = make_palindrome_general(input_data)
        result_general_palindrome_general = make_palindrome_general(input_data_for_general)

        # then
        self.assertEqual(result_palindrome, expected_output)
        self.assertEqual(result_general_palindrome, expected_output)
        self.assertEqual(result_general_palindrome_general, expected_output_for_general)

    def test_make_palindrome_odd_count(self):
        # given
        input_data = "ACCAB"
        expected_output = "ACBCA"

        input_data_for_general = "1CC1B"
        expected_output_for_general = "1CBC1"

        # when
        result_palindrome = make_palindrome(input_data)
        result_general_palindrome = make_palindrome_general(input_data)
        result_general_palindrome_general = make_palindrome_general(input_data_for_general)

        # then
        self.assertEqual(result_palindrome, expected_output)
        self.assertEqual(result_general_palindrome, expected_output)
        self.assertEqual(result_general_palindrome_general, expected_output_for_general)

    def test_make_palindrome_single_letter(self):
        # given
        input_data = "A"
        expected_output = "A"

        # when
        result_palindrome = make_palindrome(input_data)
        result_palindrome_general = make_palindrome_general(input_data)

        # then
        self.assertEqual(result_palindrome, expected_output)
        self.assertEqual(result_palindrome_general, expected_output)

    def test_make_palindrome_empty_string(self):
        # given
        input_data = ""
        expected_output = ""

        # when
        result_palindrome = make_palindrome(input_data)
        result_palindrome_general = make_palindrome_general(input_data)

        # then
        self.assertEqual(result_palindrome, expected_output)
        self.assertEqual(result_palindrome_general, expected_output)

    def test_make_palindrome_long_string(self):
        # given
        input_data = "QWERTYUIOPASDFGHJKLZXCVBNM"
        expected_output = "A"

        # when
        result_palindrome = make_palindrome(input_data)
        result_palindrome_general = make_palindrome_general(input_data)

        # then
        self.assertEqual(result_palindrome, expected_output)
        self.assertEqual(result_palindrome_general, expected_output)

    def test_make_palindrome_invalid_symbol(self):
        # (then, when, *given)
        self.assertRaises(ValueError, make_palindrome, "A1B")

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
