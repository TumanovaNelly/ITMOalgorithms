import sys
sys.path.append('../src')
from BinAdd import bin_add
import pytest

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

if __name__ == "__main__":
    pytest.main()