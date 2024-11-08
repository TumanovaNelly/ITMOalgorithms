from random import randint
from Lab2.Task8.src.MultPolynomials import *
from Utils.Time_Memory import time_data


def test_mult_polynomials_random():
    for _ in range(100):
        f = [randint(-100, 100) for _ in range(100)]
        g = [randint(-100, 100) for _ in range(100)]
        assert mult_polynomials(f, g) == mult_polynomials_naive(f, g)


def test_time():
    time = time_data(main)
    assert time < 2