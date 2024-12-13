import unittest
from random import randint

from Lab6.Task2.src.PhoneBook import CustomDict, main
from utils import time_data, memory_data


class TestCustomDict(unittest.TestCase):
    def setUp(self):
        self.custom_dict = CustomDict()

    def test_set(self):
        # given
        to_add = [(chr(randint(ord('a'), ord('z'))), randint(-10, 10)) for _ in range(100)]
        expected_current_len = 0
        for key, value in to_add:
            # when
            if key not in self.custom_dict: expected_current_len += 1
            self.custom_dict[key] = value

            # then
            self.assertIn(key, self.custom_dict)
            self.assertEqual(value, self.custom_dict[key])
            self.assertEqual(len(self.custom_dict), expected_current_len)

    def test_delete(self):
        # given
        to_add = [(chr(randint(ord('a'), ord('z'))), randint(-10, 10)) for _ in range(100)]
        for key, value in to_add:
            self.custom_dict[key] = value
        expected_current_len = len(self.custom_dict)

        to_delete = [chr(randint(ord('a'), ord('z'))) for _ in range(100)]

        for key in to_delete:
            # when
            if key in self.custom_dict:
                del self.custom_dict[key]
                expected_current_len -= 1

                # then
                self.assertNotIn(key, self.custom_dict)
            else:
                # then
                self.assertRaises(KeyError, self.custom_dict.__delitem__, key)

            # then
            self.assertEqual(len(self.custom_dict), expected_current_len)

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
