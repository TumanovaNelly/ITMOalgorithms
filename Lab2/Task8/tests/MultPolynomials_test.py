import unittest
from random import randint

from Lab2.Task8.src.MultPolynomials import mult_polynomials, mult_polynomials_naive, main
from utils import time_data, memory_data


class TestMultPolynomials(unittest.TestCase):
    def test_mult_polynomials_random(self):
        for _ in range(100):
            # given
            f = [randint(-100, 100) for _ in range(100)]
            g = [randint(-100, 100) for _ in range(100)]
            expected_result = mult_polynomials_naive(f, g)

            # when
            result = mult_polynomials(f, g)

            # then
            self.assertEqual(result, expected_result)

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 6)
        self.assertLess(peak, 6)


if __name__ == '__main__':
    unittest.main()
