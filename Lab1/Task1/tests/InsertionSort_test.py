from Lab1.Task1.src.InsertionSort import insertion_sort, insertion_sort_bin_pow
from random import randint
import pytest

def test_already_sorted():
    lst1 = [1, 2, 3, 4, 5]
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == [1, 2, 3, 4, 5]

def test_reverse_order():
    lst1 = [5, 4, 3, 2, 1]
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == [1, 2, 3, 4, 5]

def test_random_order():
    lst1 = [3, 1, 4, 1, 5, 9, 2]
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == [1, 1, 2, 3, 4, 5, 9]

def test_duplicate_elements():
    lst1 = [2, 2, 2, 2, 2]
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == [2, 2, 2, 2, 2]

def test_empty_list():
    lst1 = []
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == []

def test_single_element():
    lst1 = [42]
    lst2 = lst1[:]
    insertion_sort(lst1)
    insertion_sort_bin_pow(lst2)
    assert lst1 == lst2 == [42]


def test_random():
    for _ in range(100):
        lst = [randint(-100, 100) for _ in range(randint(0, 100))]
        lst1 = lst[:]
        lst2 = lst[:]
        lst.sort()
        insertion_sort(lst1)
        insertion_sort_bin_pow(lst2)
        assert lst1 == lst2 == lst



if __name__ == "__main__":
    pytest.main()