import unittest

from Lab4.Task8.src.Calculate import calculate, main
from utils import time_data, memory_data


class TestCalculate(unittest.TestCase):
    def test_simple_expressions(self):
        # given
        expressions = [
            ['42'],
            ['2', '3', '+'],
            ['5', '2', '-'],
            ['4', '6', '*']
        ]
        expected_results = [42, 5, 3, 24]

        for index, expression in enumerate(expressions):
            # when
            result = calculate(expression)

            # then
            self.assertEqual(result, expected_results[index])

    def test_complex_expressions(self):
        # given
        expressions = [
            # (8 + 9) * (1 - 7) = -6 * 17
            ['8', '9', '+', '1', '7', '-', '*'],
            # 100 - (4 + 5 * (2 + 3) * 2 - 3) * 3 = 100 - 51 * 3
            ['100', '4', '5', '2', '3', '+', '2', '*', '*', '+', '3', '-', '3', '*', '-']]
        expected_results = [-102, -53]

        for index, expression in enumerate(expressions):
            # when
            result = calculate(expression)

            # then
            self.assertEqual(result, expected_results[index])

    def test_invalid_operator(self):
        expression = ['2', '3', '/', '+']
        self.assertRaises(KeyError, calculate, expression)

    def test_empty_expression(self):
        expression = []
        self.assertRaises(IndexError, calculate, expression)

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
