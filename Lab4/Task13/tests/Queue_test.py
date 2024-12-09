import unittest
from Lab4.Task13.src.Queue import Queue


class TestStack(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_push(self):
        # given
        to_push = [1, 2, 3]
        expected_lens = [1, 2, 3]
        for index, item in enumerate(to_push):
            # when
            self.queue.push(item)

            # then
            self.assertEqual(len(self.queue.queue), expected_lens[index])

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())

    def test_pop(self):
        self.assertRaises(IndexError, self.queue.pop)
        for _ in range(5):
            # given
            to_push = [1, 2, 3]
            for item in to_push:
                self.queue.push(item)
            expected_pops = [1, 2, 3]
            expected_lens = [2, 1, 0]

            for index, expected_pop in enumerate(expected_pops):
                # when
                pop_elem = self.queue.pop()

                # then
                self.assertEqual(pop_elem, expected_pop)
                self.assertEqual(len(self.queue.queue), expected_lens[index])
            # then
            self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
