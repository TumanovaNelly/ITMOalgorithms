import unittest
from Lab4.Task8.src.Calculate import calculate, main
from utils import time_data, memory_data


class TestCalculate(unittest.TestCase):

    def test_addition(self):
        expression = ['2', '3', '+']
        self.assertEqual(calculate(expression), 5)

    def test_subtraction(self):
        expression = ['5', '2', '-']
        self.assertEqual(calculate(expression), 3)

    def test_multiplication(self):
        expression = ['4', '6', '*']
        self.assertEqual(calculate(expression), 24)

    def test_complex_expression(self):
        # (8 + 9) * (1 - 7) = -6 * 17
        expression = ['8', '9', '+', '1', '7', '-', '*']
        self.assertEqual(calculate(expression), -102)

        # 100 - (4 + 5 * (2 + 3) * 2 - 3) * 3 = 100 - 51 * 3
        expression = ['100', '4', '5', '2', '3', '+', '2', '*', '*', '+', '3', '-', '3', '*', '-']
        self.assertEqual(calculate(expression), -53)

    def test_single_number(self):
        expression = ['42']
        self.assertEqual(calculate(expression), 42)

    def test_invalid_operator(self):
        expression = ['2', '3', '/', '+']
        with self.assertRaises(KeyError):
            calculate(expression)

    def test_empty_expression(self):
        expression = []
        with self.assertRaises(IndexError):
            calculate(expression)

    def test_time(self):
        self.assertTrue(time_data(main) < 2)

    def test_memory_data(self):
        cur, peak = memory_data(main)
        self.assertTrue(cur < 5)
        self.assertTrue(peak < 5)

if __name__ == '__main__':
    unittest.main()
