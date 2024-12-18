import unittest

from Lab7.Task1.src.Coins import main, count_coins_with_borders_optimized, count_coins_no_borders
from utils import time_data, memory_data


class TestCoinsCount(unittest.TestCase):
    def test_count_coins_no_borders(self):
        # given
        coins_sets = [[1, 3, 4], [1, 2, 5], [3, 6, 9]]
        prices = [0, 1, 2, 5, 34, 60]
        expected_results = [[0, 0, 0],
                            [1, 1, None],
                            [2, 1, None],
                            [2, 1, None],
                            [9, 8, None],
                            [15, 12, 7]]

        for line, price in enumerate(prices):
            for column, coins in enumerate(coins_sets):
                # when
                result = count_coins_no_borders(price, coins)

                # then
                self.assertEqual(result, expected_results[line][column])

    def test_count_coins_with_borders(self):
        # given
        coins_sets = [{1: 1, 3: 1, 4: 1}, {1: 3, 2: 20, 5: 1}, {3: 10, 6: 10, 9: 1}]
        prices = [0, 1, 2, 5, 34, 60]
        expected_results = [[0, 0, 0],
                            [1, 1, None],
                            [None, 1, None],
                            [2, 1, None],
                            [None, 16, None],
                            [None, None, 10]]

        for line, price in enumerate(prices):
            for column, coins in enumerate(coins_sets):
                # when
                result = count_coins_with_borders_optimized(price, coins)

                # then
                self.assertEqual(result, expected_results[line][column])

    def test_time(self):
        # when
        time = time_data(main)
        # then
        self.assertLess(time, 1)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)
        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == "__main__":
    unittest.main()
