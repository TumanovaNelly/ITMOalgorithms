import unittest
from random import randint

from Lab5.Task1.src.CheckHeap import check_heap
from Lab5.Task4.src.Heapify import Heap, main
from utils import time_data, memory_data


class TestHeapify(unittest.TestCase):
    def test_heapify_random(self):
        # given
        data = [randint(-1000, 1000) for i in range(1000)]

        # when
        heap = Heap(data)

        # then
        self.assertTrue(check_heap(heap._Heap__nodes))

    def test_simple_data(self):
        # given
        expressions = [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1]
        ]
        expected_results = [
            [],
            [(1, 4), (0, 1), (1, 3)]
        ]

        for index, expression in enumerate(expressions):
            # when
            result = Heap(expression).permutations_to_heap

            # then
            self.assertEqual(result, expected_results[index])

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
