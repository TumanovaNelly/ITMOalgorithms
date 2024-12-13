import unittest

from Lab6.Task7.src.Stones import count_index, main
from utils import time_data, memory_data


class TestStones(unittest.TestCase):
    def test_stones_prime(self):
        # given
        string = "abacaba"
        beauty_dicts = [{"a": ["a"]}, {"b": ["a", "b"], "c": ["a"]}]
        expected_result = [6, 7]

        for index, beauty_dict in enumerate(beauty_dicts):
            # when
            result = count_index(string, beauty_dict)

            # then
            self.assertEqual(result, expected_result[index])

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