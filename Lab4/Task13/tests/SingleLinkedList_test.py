import sys
import unittest
from io import StringIO

from Lab4.Task13.src.SingleLinkedList import SingleLinkedList



class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()


    def test_initialization(self):
        self.assertEqual(self.linked_list.length, 0)
        self.assertIsNone(self.linked_list.head)


    def test_push(self):
        self.linked_list.push(1)
        self.assertEqual(self.linked_list.length, 1)
        self.assertEqual(self.linked_list.head.value, 1)

        self.linked_list.push(2)
        self.assertEqual(self.linked_list.length, 2)
        self.assertEqual(self.linked_list.head.value, 2)


    def test_pop(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop()

        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        self.assertEqual(self.linked_list.pop(), 3)
        self.assertEqual(self.linked_list.length, 2)

        self.assertEqual(self.linked_list.pop(), 2)
        self.assertEqual(self.linked_list.length, 1)

        self.assertEqual(self.linked_list.pop(), 1)
        self.assertEqual(self.linked_list.length, 0)


    def test_find(self):
        self.linked_list.push(10)
        self.linked_list.push(20)
        self.linked_list.push(30)

        self.assertIsNotNone(self.linked_list.find(20))
        with self.assertRaises(ValueError):
            self.linked_list.find(40)
        self.assertEqual(self.linked_list.find(10).value, 10)


    def test_remove_after(self):
        self.linked_list.push(10)
        self.linked_list.push(20)
        self.linked_list.push(30)

        self.assertEqual(self.linked_list.remove_after(30), 20)
        with self.assertRaises(ValueError):
            self.linked_list.find(20)

        self.assertEqual(self.linked_list.length, 2)

        # Тест на удаление после последнего элемента
        with self.assertRaises(IndexError):
            self.linked_list.remove_after(10)

        # Тест на удаление после несуществующего элемента
        with self.assertRaises(ValueError):
            self.linked_list.remove_after(100)


    def test_print(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        captured_output = StringIO()
        sys.stdout = captured_output  # Перехват вывода в stdout
        self.linked_list.print()
        sys.stdout = sys.__stdout__  # Восстановление stdout

        self.assertEqual(captured_output.getvalue(), "3 2 1 ")


if __name__ == '__main__':
    unittest.main()