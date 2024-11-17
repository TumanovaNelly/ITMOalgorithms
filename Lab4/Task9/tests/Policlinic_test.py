import unittest
from typing import TypeVar
from Lab4.Task9.src.Polyclinic import Queue

T = TypeVar('T')


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()


    def test_initial_length(self):
        self.assertEqual(len(self.queue), 0)


    def test_push_back(self):
        self.queue.push_back(1)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.mid.value, 1)
        self.assertEqual(self.queue.tail.value, 1)

        self.queue.push_back(2)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.mid.value, 1)
        self.assertEqual(self.queue.tail.value, 2)

        self.queue.push_back(3)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.mid.value, 2)
        self.assertEqual(self.queue.tail.value, 3)


    def test_push_mid(self):
        self.queue.push_back(1)
        self.queue.push_back(2)
        self.queue.push_back(4)
        self.queue.push_back(5)
        self.queue.push_mid(3)

        self.assertEqual(len(self.queue), 5)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.mid.value, 3)
        self.assertEqual(self.queue.tail.value, 5)

        self.queue.push_mid(10)
        self.assertEqual(len(self.queue), 6)
        self.assertEqual(self.queue.head.value, 1)
        self.assertEqual(self.queue.mid.value, 3)
        self.assertEqual(self.queue.mid.next.value, 10)
        self.assertEqual(self.queue.tail.value, 5)


    def test_pop_front(self):
        self.queue.push_back(1)
        self.queue.push_back(2)
        self.queue.push_back(3)

        self.assertEqual(self.queue.pop_front(), 1)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.head.value, 2)
        self.assertEqual(self.queue.mid.value, 2)
        self.assertEqual(self.queue.tail.value, 3)

        self.assertEqual(self.queue.pop_front(), 2)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.head.value, 3)
        self.assertEqual(self.queue.mid.value, 3)
        self.assertEqual(self.queue.tail.value, 3)

        self.assertEqual(self.queue.pop_front(), 3)
        self.assertEqual(len(self.queue), 0)
        self.assertIsNone(self.queue.head)
        self.assertIsNone(self.queue.mid)
        self.assertIsNone(self.queue.tail)


    def test_pop_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.pop_front()


    def test_print_queue(self):
        self.queue.push_back(1)
        self.queue.push_back(2)
        self.queue.push_back(3)

        # Захватываем вывод в консоль
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.queue.print()

        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "1 2 3 \n")


if __name__ == '__main__':
    unittest.main()
