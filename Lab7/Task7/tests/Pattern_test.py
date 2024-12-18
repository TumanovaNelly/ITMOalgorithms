import unittest

from Lab7.Task7.src.Pattern import is_match_memory_optimized, main
from utils import time_data, memory_data


class TestPattern(unittest.TestCase):
    def test_is_match_true(self):
        # given
        patterns = ['k*t?n', '**e?', 'kit*', '*', '??????']
        word = 'kitten'

        for pattern in patterns:
            # when
            result = is_match_memory_optimized(word, pattern)

            # then
            self.assertTrue(result)

    def test_is_match_false(self):
        # given
        patterns = ['k?t?n', '**e', 'kit*p', '?', '??i??']
        word = 'kitten'

        for pattern in patterns:
            # when
            result = is_match_memory_optimized(word, pattern)

            # then
            self.assertFalse(result)

    def test_time(self):
        # when
        time = time_data(main)
        # then
        self.assertLess(time, 1)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)
        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == "__main__":
    unittest.main()
