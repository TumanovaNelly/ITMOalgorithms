import sys
import unittest
from io import StringIO

from Lab4.Task13.src.List import List


class TestList(unittest.TestCase):
    def setUp(self):
        self.linked_list = List()

    def test_initialization(self):
        self.assertEqual(len(self.linked_list), 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_push_back(self):
        to_push_back = [1, 2, 3, 4, 5]
        expected_lens = [1, 2, 3, 4, 5]
        expected_head_tail_values = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
        for index, item in enumerate(to_push_back):
            # when
            self.linked_list.push_back(item)

            # then
            self.assertEqual(len(self.linked_list), expected_lens[index])
            self.assertEqual(self.linked_list.head.value, expected_head_tail_values[index][0])
            self.assertEqual(self.linked_list.tail.value, expected_head_tail_values[index][1])

    def test_push_front(self):
        to_push_front = [1, 2, 3, 4, 5]
        expected_lens = [1, 2, 3, 4, 5]
        expected_head_tail_values = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
        for index, item in enumerate(to_push_front):
            # when
            self.linked_list.push_front(item)

            # then
            self.assertEqual(len(self.linked_list), expected_lens[index])
            self.assertEqual(self.linked_list.head.value, expected_head_tail_values[index][0])
            self.assertEqual(self.linked_list.tail.value, expected_head_tail_values[index][1])

    def test_pop_back(self):
        self.assertRaises(IndexError, self.linked_list.pop_back)

        for _ in range(5):
            # given
            to_push_back = [1, 2, 3]
            for item in to_push_back:
                self.linked_list.push_back(item)

            expected_pops_back = [3, 2, 1]
            expected_lens = [2, 1, 0]
            expected_head_tail_values = [(1, 2), (1, 1)]

            for index, item in enumerate(to_push_back):
                # when
                pop_elem = self.linked_list.pop_back()

                # then
                self.assertEqual(pop_elem, expected_pops_back[index])
                self.assertEqual(len(self.linked_list), expected_lens[index])
                if index < len(to_push_back) - 1:
                    self.assertEqual(self.linked_list.head.value, expected_head_tail_values[index][0])
                    self.assertEqual(self.linked_list.tail.value, expected_head_tail_values[index][1])

            # then
            self.assertIsNone(self.linked_list.head)
            self.assertIsNone(self.linked_list.tail)


    def test_pop_front(self):
        self.assertRaises(IndexError, self.linked_list.pop_front)

        for _ in range(5):
            # given
            to_push_back = [1, 2, 3]
            for item in to_push_back:
                self.linked_list.push_back(item)

            expected_pops_front = [1, 2, 3]
            expected_lens = [2, 1, 0]
            expected_head_tail_values = [(2, 3), (3, 3)]

            for index, item in enumerate(to_push_back):
                # when
                pop_elem = self.linked_list.pop_front()

                # then
                self.assertEqual(pop_elem, expected_pops_front[index])
                self.assertEqual(len(self.linked_list), expected_lens[index])
                if index < len(to_push_back) - 1:
                    self.assertEqual(self.linked_list.head.value, expected_head_tail_values[index][0])
                    self.assertEqual(self.linked_list.tail.value, expected_head_tail_values[index][1])

            # then
            self.assertIsNone(self.linked_list.head)
            self.assertIsNone(self.linked_list.tail)

    def test_find(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push_back(item)

        # when
        found_node = self.linked_list.find(2)

        # then
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.value, 2)
        self.assertRaises(ValueError, self.linked_list.find, 200)


    def test_remove_after(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push_back(item)

        # when
        self.linked_list.remove_after(2)

        # then
        self.assertRaises(ValueError, self.linked_list.find, 3)
        self.assertRaises(IndexError, self.linked_list.remove_after, 2)
        self.assertRaises(ValueError, self.linked_list.remove_after, 200)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 2)

    def test_remove_before(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push_back(item)

        # when
        self.linked_list.remove_before(2)

        # then
        self.assertRaises(ValueError, self.linked_list.find, 1)
        self.assertRaises(IndexError, self.linked_list.remove_before, 2)
        self.assertRaises(ValueError, self.linked_list.remove_after, 200)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.tail.value, 3)

    def test_print(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push_back(item)

        # when
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linked_list.print()
        sys.stdout = sys.__stdout__

        # then
        self.assertEqual(captured_output.getvalue(), "1 2 3 \n")


if __name__ == '__main__':
    unittest.main()
