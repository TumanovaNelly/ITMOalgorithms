import sys
import unittest
from io import StringIO

from Lab4.Task13.src.List import List


class TestList(unittest.TestCase):
    def setUp(self):
        self.linked_list = List()


    def test_initialization(self):
        self.assertEqual(self.linked_list.length, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)


    def test_push_back(self):
        self.linked_list.push_back(10)
        self.linked_list.push_back(20)
        self.assertEqual(self.linked_list.head.value, 10)
        self.assertEqual(self.linked_list.tail.value, 20)
        self.assertEqual(self.linked_list.length, 2)


    def test_push_front(self):
        self.linked_list.push_front(10)
        self.linked_list.push_front(20)
        self.assertEqual(self.linked_list.head.value, 20)
        self.assertEqual(self.linked_list.tail.value, 10)
        self.assertEqual(self.linked_list.length, 2)


    def test_pop_back(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop_back()

        self.linked_list.push_back(10)
        self.linked_list.push_back(20)
        self.assertEqual(self.linked_list.pop_back(), 20)
        self.assertEqual(self.linked_list.pop_back(), 10)


    def test_pop_front(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop_front()

        self.linked_list.push_front(10)
        self.linked_list.push_front(20)
        self.assertEqual(self.linked_list.pop_front(), 20)
        self.assertEqual(self.linked_list.pop_front(), 10)


    def test_find(self):
        self.linked_list.push_back(10)
        self.linked_list.push_back(20)
        self.assertIsNotNone(self.linked_list.find(10))
        with self.assertRaises(ValueError):
            self.linked_list.find(200)


    def test_remove_after(self):
        self.linked_list.push_back(10)
        self.linked_list.push_back(20)
        self.linked_list.push_back(30)
        self.linked_list.remove_after(20)
        with self.assertRaises(ValueError):
            self.linked_list.find(30)

        with self.assertRaises(ValueError):
            self.linked_list.remove_after(40)
        with self.assertRaises(IndexError):
            self.linked_list.remove_after(20)

        self.assertEqual(self.linked_list.head.value, 10)
        self.assertEqual(self.linked_list.tail.value, 20)


    def test_remove_before(self):
        self.linked_list.push_back(10)
        self.linked_list.push_back(20)
        self.linked_list.push_back(30)
        self.linked_list.remove_before(20)
        with self.assertRaises(ValueError):
            self.linked_list.find(10)

        with self.assertRaises(ValueError):
            self.linked_list.remove_before(40)
        with self.assertRaises(IndexError):
            self.linked_list.remove_before(20)

        self.assertEqual(self.linked_list.head.value, 20)
        self.assertEqual(self.linked_list.tail.value, 30)


    def test_print(self):
        self.linked_list.push_back(1)
        self.linked_list.push_back(2)
        self.linked_list.push_back(3)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linked_list.print()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "1 2 3 ")

if __name__ == '__main__':
    unittest.main()