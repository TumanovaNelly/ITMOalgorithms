import unittest
from Lab7.Task1.src.Coins import main, count_coins_with_borders_optimized, count_coins_no_borders
from utils import time_data, memory_data


class TestCoins(unittest.TestCase):
    def test_count_coins(self):
        self.assertEqual(count_coins_no_borders(34, [1, 3, 4]), 9)

if __name__ == "__main__":
    unittest.main()
