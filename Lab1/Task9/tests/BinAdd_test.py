import pytest

from Lab1.Task9.src.BinAdd import bin_add, main
from utils import time_data, memory_data


def test_bin_add_same_length():
    assert bin_add([1, 0, 1], [1, 1, 0]) == [1, 0, 1, 1]


def test_bin_add_different_length():
    assert bin_add([1, 0], [1, 1, 1]) == [1, 0, 0, 1]


def test_bin_add_all_zeros():
    assert bin_add([0, 0, 0], [0, 0, 0]) == [0, 0, 0, 0]


def test_bin_add_one_bit():
    assert bin_add([1], [1]) == [1, 0]


def test_bin_add_large_numbers():
    assert bin_add([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 0]


def test_bin_add_invalid_input():
    with pytest.raises(ValueError):
        bin_add([1, 0, 2], [0, 1, 0])


def test_bin_add_invalid_input_non_binary():
    with pytest.raises(ValueError):
        bin_add([1, 0, 1], [1, 0, 5])


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1