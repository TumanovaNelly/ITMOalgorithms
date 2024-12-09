import sys
import unittest
from io import StringIO

from Lab4.Task13.src.SingleLinkedList import SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def test_initialization(self):
        self.assertEqual(len(self.linked_list), 0)
        self.assertIsNone(self.linked_list.head)

    def test_push(self):
        to_push = [1, 2, 3]
        expected_lens = [1, 2, 3]
        for index, item in enumerate(to_push):
            # when
            self.linked_list.push(item)

            # then
            self.assertEqual(len(self.linked_list), expected_lens[index])
            self.assertEqual(self.linked_list.head.value, item)

    def test_pop(self):
        self.assertRaises(IndexError, self.linked_list.pop)

        for _ in range(5):
            # given
            to_push = [1, 2, 3]
            for item in to_push:
                self.linked_list.push(item)

            expected_pops = [3, 2, 1]
            expected_lens = [2, 1, 0]
            expected_head_values = [2, 1]

            for i in range(len(to_push)):
                # when
                pop_elem = self.linked_list.pop()

                # then
                self.assertEqual(pop_elem, expected_pops[i])
                self.assertEqual(len(self.linked_list), expected_lens[i])
                if i < len(to_push) - 1:
                    self.assertEqual(self.linked_list.head.value, expected_head_values[i])

            # then
            self.assertIsNone(self.linked_list.head)

    def test_find(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push(item)

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
            self.linked_list.push(item)

        # when
        self.linked_list.remove_after(2)

        # then
        self.assertRaises(ValueError, self.linked_list.find, 1)
        self.assertRaises(IndexError, self.linked_list.remove_after, 2)
        self.assertRaises(ValueError, self.linked_list.remove_after, 200)
        self.assertEqual(self.linked_list.head.value, 3)
        self.assertEqual(self.linked_list.head.next.value, 2)
        self.assertIsNone(self.linked_list.head.next.next)

    def test_print(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.linked_list.push(item)

        # when
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linked_list.print()
        sys.stdout = sys.__stdout__

        # then
        self.assertEqual(captured_output.getvalue(), "3 2 1 \n")


if __name__ == '__main__':
    unittest.main()
