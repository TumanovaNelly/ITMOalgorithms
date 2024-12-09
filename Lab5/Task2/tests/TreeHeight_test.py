import unittest
from typing import List

from Lab5.Task2.src.TreeHeight import build_tree, main
from utils import time_data, memory_data


class TestTree(unittest.TestCase):
    def test_empty_tree(self):
        # given
        elements_data: List[int] = []

        # when
        tree = build_tree(elements_data)

        # then
        self.assertIsNone(tree)

    def test_simple_data(self):
        # given
        expressions = [
            [-1],
            [4, -1, 4, 1, 1],
            [-1, 0, 4, 0, 3],
            [-1, 0, 0, 1, 1],
            [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        ]
        expected_height_results = [1, 3, 4, 3, 4]

        for index, expression in enumerate(expressions):
            # when
            result_height = build_tree(expression).height

            # then
            self.assertEqual(result_height, expected_height_results[index])

    def test_high_tree_height(self):
        # given
        elements_data = [i - 1 for i in range(100000)]
        tree = build_tree(elements_data)

        # when
        height = tree.height

        # then
        self.assertEqual(height, 100000)

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


if __name__ == "__main__":
    unittest.main()
