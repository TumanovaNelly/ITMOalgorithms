import unittest
from Lab4.Task13.src.Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        # given
        to_push = [1, 2, 3]
        expected_lens = [1, 2, 3]
        for index, item in enumerate(to_push):
            # when
            self.stack.push(item)

            # then
            self.assertEqual(len(self.stack.stack), expected_lens[index])

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_pop(self):
        self.assertRaises(IndexError, self.stack.pop)
        for _ in range(5):
            # given
            to_push = [1, 2, 3]
            for item in to_push:
                self.stack.push(item)
            expected_pops = [3, 2, 1]
            expected_lens = [2, 1, 0]

            for index, expected_pop in enumerate(expected_pops):
                # when
                pop_elem = self.stack.pop()

                # then
                self.assertEqual(pop_elem, expected_pop)
                self.assertEqual(len(self.stack.stack), expected_lens[index])
            # then
            self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
