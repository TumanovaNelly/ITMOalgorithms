import unittest
from typing import List
from Lab5.Task2.src.TreeHeight import build_tree, TreeNode, Tree

class TestTree(unittest.TestCase):
    def test_empty_tree(self):
        # given
        elements_data: List[int] = []

        # when
        tree = build_tree(elements_data)

        # then
        self.assertIsNone(tree)

    def test_build_tree_single_node(self):
        # given
        elements_data = [-1]
        tree = build_tree(elements_data)

        # when
        height = tree.height

        # then
        self.assertEqual(height, 1)

    def test_build_tree_simple(self):
        # given
        elements_data = [-1, 0, 0, 1, 1]
        tree = build_tree(elements_data)

        # when
        height = tree.height

        # then
        self.assertEqual(height, 3)

    def test_build_tree_complex(self):
        # given
        elements_data = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        tree = build_tree(elements_data)

        # when
        height = tree.height

        # then
        self.assertEqual(height, 4)

    def test_high_tree_height(self):
        # given
        elements_data = [i - 1 for i in range(100000)]
        tree = build_tree(elements_data)

        # when
        height = tree.height

        # then
        self.assertEqual(height, 100000)


if __name__ == "__main__":
    unittest.main()
