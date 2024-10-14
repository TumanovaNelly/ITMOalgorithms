from Lab1.Task4.src.Find import find
import pytest

def test_find_found():
    lst = [1, 2, 3, 4, 5]
    value = 3
    assert find(lst, value) == [3]  

def test_find_not_found():
    lst = [1, 2, 3, 4, 5]
    value = 6
    assert find(lst, value) == [-1]  

def test_find_first_element():
    lst = [1, 2, 3, 4, 5]
    value = 1
    assert find(lst, value) == [1]  

def test_find_last_element():
    lst = [1, 2, 3, 4, 5]
    value = 5
    assert find(lst, value) == [5] 

def test_find_empty_list():
    lst = []
    value = 1
    assert find(lst, value) == [-1] 

def test_find_multiple_occurrences():
    lst = [1, 2, 3, 2, 5]
    value = 2
    assert find(lst, value) == [2, 4]

if __name__ == "__main__":
    pytest.main()