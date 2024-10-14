import sys
sys.path.append('../src')
from SelectionSort import selection_sort
import pytest

def test_already_sorted():
    lst = [1, 2, 3, 4, 5]
    selection_sort(lst)
    assert lst == [1, 2, 3, 4, 5]

def test_reverse_order():
    lst = [5, 4, 3, 2, 1]
    selection_sort(lst)
    assert lst == [1, 2, 3, 4, 5]

def test_random_order():
    lst = [3, 1, 4, 1, 5, 9, 2]
    selection_sort(lst)
    assert lst == [1, 1, 2, 3, 4, 5, 9]

def test_duplicate_elements():
    lst = [2, 2, 2, 2, 2]
    selection_sort(lst)
    assert lst == [2, 2, 2, 2, 2]

def test_empty_list():
    lst = []
    selection_sort(lst)
    assert lst == []

def test_single_element():
    lst = [42]
    selection_sort(lst)
    assert lst == [42]

if __name__ == "__main__":
    pytest.main()