from random import randint

from Lab2.Task4.src.BinPow import bin_pow


def test_bin_pow():
    for _ in range(1000):
        lst = [randint(-100, 100) for _ in range(1000)]
        lst.sort()
        value = randint(-100, 100)

        index = bin_pow(lst, value)
        if index == -1:
            assert value not in lst
        else:
            assert lst[index] == value