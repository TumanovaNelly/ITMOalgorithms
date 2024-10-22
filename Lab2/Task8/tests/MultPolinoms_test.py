from random import randint
from Lab2.Task8.src.MultPolynomials import mult_polynomials, mult_polynomials_naive

def test_mult_polynomials_random():
    for _ in range(100):
        f = [randint(-100, 100) for _ in range(100)]
        g = [randint(-100, 100) for _ in range(100)]
        assert mult_polynomials(f, g) == mult_polynomials_naive(f, g)