import unittest
from random import randint

from Lab6.Task4.src.AssociativeArray import AssociativeArray, main
from utils import time_data, memory_data


class TestCustomDict(unittest.TestCase):
    def setUp(self):
        self.array = AssociativeArray()

    def test_set(self):
        # given
        to_add = [(chr(randint(ord('a'), ord('z'))), randint(-10, 10)) for _ in range(100)]
        expected_current_len = 0
        for index, (key, value) in enumerate(to_add):
            # when
            if key not in self.array: expected_current_len += 1
            self.array[key] = value

            # then
            self.assertIn(key, self.array)
            self.assertEqual(value, self.array[key])
            self.assertEqual(len(self.array), expected_current_len)

    def test_delete(self):
        # given
        to_add = [(chr(randint(ord('a'), ord('z'))), randint(-10, 10)) for _ in range(100)]
        for key, value in to_add:
            self.array[key] = value
        expected_current_len = len(self.array)

        to_delete = [chr(randint(ord('a'), ord('z'))) for _ in range(100)]

        for key in to_delete:
            # when
            if key in self.array:
                del self.array[key]
                expected_current_len -= 1

                # then
                self.assertNotIn(key, self.array)
            else:
                # then
                self.assertRaises(KeyError, self.array.__delitem__, key)

            # then
            self.assertEqual(len(self.array), expected_current_len)

    def test_links(self):
        self.assertIsNone(self.array.head)
        self.assertIsNone(self.array.tail)

        # given
        to_add = [(chr(randint(ord('a'), ord('z'))), randint(-10, 10)) for _ in range(100)]
        for key, value in to_add:
            self.array[key] = value
        expected_sequence_keys = set()
        expected_sequence_values = []
        for key, value in reversed(to_add):
            if key not in expected_sequence_keys:
                expected_sequence_values.append(value)
                expected_sequence_keys.add(key)

        # when
        for index, key in enumerate(self.array):
            # then
            self.assertEqual(self.array[key], expected_sequence_values[-index - 1])
            if index > 0:
                self.assertEqual(self.array[self.array.previous(key)],
                                 expected_sequence_values[-index] if index > 0 else None)
            else: self.assertIsNone(self.array.previous(key))

            if index < len(self.array) - 1:
                self.assertEqual(self.array[self.array.next(key)],
                                 expected_sequence_values[-index - 2] if index < len(self.array) - 1 else None)
            else: self.assertIsNone(self.array.next(key))

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
