import unittest
from random import randint

from Lab5.Task7.src.Heap import Heap, main
from utils import time_data, memory_data


class TestHeap(unittest.TestCase):
    def test_heap_sorting(self):
        # given
        lst = [randint(-1000, 1000) for _ in range(100)]
        sorted_lst = sorted(lst)
        heap = Heap(lst)

        # when
        result = []
        for _ in range(len(lst)):
            result.append(heap.extract_min())

        # then
        self.assertEqual(result, sorted_lst)

    def test_heap_sorting_reversed(self):
        # given
        lst = [randint(-1000, 1000) for _ in range(10)]
        sorted_lst = sorted(lst)
        heap = Heap(lst, is_reversed=True)

        # when
        result = []
        for _ in range(len(lst)):
            result.append(heap.extract_min())

        # then
        self.assertEqual(result, list(reversed(sorted_lst)))

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
        self.assertLess(peak, 30)


if __name__ == '__main__':
    unittest.main()
