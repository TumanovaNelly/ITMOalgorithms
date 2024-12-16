import unittest
from random import randint

from Lab6.Task1.src.CustomSet import CustomSet, main
from utils import time_data, memory_data


class TestCustomSet(unittest.TestCase):
    def setUp(self):
        self.custom_set = CustomSet()

    def test_add(self):
        # given
        to_add = [randint(-10, 10) for _ in range(100)]
        expected_current_len = 0
        for item in to_add:
            # when
            if item not in self.custom_set: expected_current_len += 1
            self.custom_set.add(item)
            # then
            self.assertIn(item, self.custom_set)
            self.assertEqual(len(self.custom_set), expected_current_len)

    def test_remove(self):
        # given
        to_add = [randint(-10, 10) for _ in range(100)]
        for item in to_add:
            self.custom_set.add(item)
        expected_current_len = len(self.custom_set)
        to_remove = [randint(-10, 10) for _ in range(100)]
        for item in to_remove:
            # when
            if item in self.custom_set:
                self.custom_set.remove(item)
                expected_current_len -= 1
                # then
                self.assertNotIn(item, self.custom_set)
            else:
                # then
                self.assertRaises(KeyError, self.custom_set.remove, item)
            # then
            self.assertEqual(len(self.custom_set), expected_current_len)

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
