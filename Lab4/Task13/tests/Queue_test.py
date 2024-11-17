import unittest
from Lab4.Task13.src.Queue import Queue


class TestStack(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_push(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(len(self.queue.queue), 3)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())

    def test_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertTrue(self.queue.is_empty())

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.queue.pop()

    def test_len(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push(5)
        self.assertEqual(len(self.queue.queue), 1)
        self.queue.pop()
        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
