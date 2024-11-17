import unittest
from Lab4.Task13.src.Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack.stack), 3)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_len(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertEqual(len(self.stack.stack), 1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
