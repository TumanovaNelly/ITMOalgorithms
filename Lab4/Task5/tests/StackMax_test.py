import unittest
from Lab4.Task5.src.StackMax import Stack, main
from utils import time_data, memory_data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_and_max(self):
        self.stack.push(10)
        self.assertEqual(self.stack.max(), 10)

        self.stack.push(20)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(5)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(20)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(15)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(25)
        self.assertEqual(self.stack.max(), 25)

    def test_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.max()
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_sequential_operations(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(15)
        self.stack.push(35)
        self.stack.push(35)

        self.assertEqual(self.stack.max(), 35)
        self.assertEqual(self.stack.pop(), 35)
        self.assertEqual(self.stack.max(), 35)
        self.assertEqual(self.stack.pop(), 35)
        self.assertEqual(self.stack.max(), 20)
        self.assertEqual(self.stack.pop(), 15)
        self.assertEqual(self.stack.max(), 20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.max(), 10)
        self.assertEqual(self.stack.pop(), 10)

        self.stack.push(45)
        self.stack.push(35)
        self.assertEqual(self.stack.max(), 45)
        self.assertEqual(self.stack.pop(), 35)
        self.assertEqual(self.stack.max(), 45)
        self.assertEqual(self.stack.pop(), 45)

    def test_time(self):
        assert time_data(main) < 2

    def test_memory_data(self):
        cur, peak = memory_data(main)
        assert cur < 5
        assert peak < 5


if __name__ == '__main__':
    unittest.main()
