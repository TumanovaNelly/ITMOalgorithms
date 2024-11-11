from random import randint
from Lab2.Task8.src.MultPolynomials import mult_polynomials, mult_polynomials_naive, main
from utils import time_data, memory_data


def test_mult_polynomials_random():
    for _ in range(100):
        f = [randint(-100, 100) for _ in range(100)]
        g = [randint(-100, 100) for _ in range(100)]
        assert mult_polynomials(f, g) == mult_polynomials_naive(f, g)


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1