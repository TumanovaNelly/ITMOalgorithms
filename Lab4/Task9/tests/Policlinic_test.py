import unittest
from typing import TypeVar

from Lab4.Task9.src.Polyclinic import Queue, main
from utils import time_data, memory_data

T = TypeVar('T')


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def test_initial_length(self):
        self.assertEqual(len(self.queue), 0)

    def test_push_back(self):
        # given
        to_push_back = [1, 2, 3]
        expected_lens = [1, 2, 3]
        expected_head_mid_tail_values = [(1, 1, 1), (1, 1, 2), (1, 2, 3)]

        for index, item in enumerate(to_push_back):
            # when
            self.queue.push_back(item)

            # then
            self.assertEqual(len(self.queue), expected_lens[index])
            self.assertEqual(self.queue.head.value, expected_head_mid_tail_values[index][0])
            self.assertEqual(self.queue.mid.value, expected_head_mid_tail_values[index][1])
            self.assertEqual(self.queue.tail.value, expected_head_mid_tail_values[index][2])

    def test_push_mid(self):
        # given
        to_push_back = [1, 2, 3, 4]
        for item in to_push_back:
            self.queue.push_back(item)

        to_push_mid = [10, 11, 12]
        expected_lens = [5, 6, 7]
        expected_head_mid_tail_values = [(1, 10, 4), (1, 10, 4), (1, 12, 4)]

        for index, item in enumerate(to_push_mid):
            # when
            self.queue.push_mid(item)

            # then
            self.assertEqual(len(self.queue), expected_lens[index])
            self.assertEqual(self.queue.head.value, expected_head_mid_tail_values[index][0])
            self.assertEqual(self.queue.mid.value, expected_head_mid_tail_values[index][1])
            self.assertEqual(self.queue.tail.value, expected_head_mid_tail_values[index][2])

    def test_pop_front(self):
        self.assertRaises(IndexError, self.queue.pop_front)

        for _ in range(5):
            # given
            to_push_back = [1, 2, 3]
            for item in to_push_back:
                self.queue.push_back(item)

            expected_pops_front = [1, 2, 3]
            expected_lens = [2, 1, 0]
            expected_head_mid_tail_values = [(2, 2, 3), (3, 3, 3)]

            for index, item in enumerate(to_push_back):
                # when
                pop_elem = self.queue.pop_front()

                # then
                self.assertEqual(pop_elem, expected_pops_front[index])
                self.assertEqual(len(self.queue), expected_lens[index])
                if index < len(to_push_back) - 1:
                    self.assertEqual(self.queue.head.value, expected_head_mid_tail_values[index][0])
                    self.assertEqual(self.queue.mid.value, expected_head_mid_tail_values[index][1])
                    self.assertEqual(self.queue.tail.value, expected_head_mid_tail_values[index][2])

            # then
            self.assertIsNone(self.queue.head)
            self.assertIsNone(self.queue.mid)
            self.assertIsNone(self.queue.tail)

    def test_print_queue(self):
        # given
        to_push_back = [1, 2, 3]
        for item in to_push_back:
            self.queue.push_back(item)

        # when
        # Захватываем вывод в консоль
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.queue.print()
        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__

        # then
        self.assertEqual(captured_output.getvalue(), "1 2 3 \n")

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == '__main__':
    unittest.main()
