import unittest

from Lab6.Task9.src.HashKiller import generate_strings, get_hash, main
from utils import time_data, memory_data


class TestHashKiller(unittest.TestCase):
    def test_check_hashes(self):
        # given
        strings_number = 10_000

        # when
        strings_sequence = generate_strings(strings_number)
        self.assertEqual(len(set(strings_sequence)), strings_number)

        for mult in range(2, 1024):
            hsh = None
            # then
            for string in strings_sequence:
                self.assertLessEqual(len(string), 2500)

                if hsh is not None:
                    self.assertEqual(hsh, get_hash(string, mult))
                else: hsh = get_hash(string, mult)

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
        self.assertLess(peak, 20)


if __name__ == '__main__':
    unittest.main()
