import unittest

from Lab4.Task5.src.StackMax import Stack, main
from utils import time_data, memory_data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_and_max(self):
        # given
        to_push = [10, 20, 5, 20, 15, 25]
        expected_mxs = [10, 20, 20, 20, 20, 25]

        for index, item in enumerate(to_push):
            # when
            self.stack.push(item)

            # then
            self.assertEqual(self.stack.max(), expected_mxs[index])

    def test_empty_stack(self):
        self.assertRaises(IndexError, self.stack.max)
        self.assertRaises(IndexError, self.stack.pop)

    def test_sequential_operations(self):
        for i in range(5):
            # given (first part)
            to_push = [10, 20, 15, 35, 35]
            for item in to_push:
                self.stack.push(item)

            expected_mx_then_pop = [(35, 35), (35, 35), (20, 15), (20, 20), (10, 10)]

            for i in range(len(to_push)):
                # when
                mx_elem, pop_elem = self.stack.max(), self.stack.pop()

                # then
                self.assertEqual(mx_elem, expected_mx_then_pop[i][0])
                self.assertEqual(pop_elem, expected_mx_then_pop[i][1])

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
