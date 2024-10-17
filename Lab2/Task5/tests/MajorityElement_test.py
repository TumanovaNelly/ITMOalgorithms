from Lab2.Task5.src.MajorityElement import majority_element_recursion, majority_element_line


def test_majority_elem():
    lst = [2, 3, 9, 2, 2]
    assert majority_element_recursion(lst) == (2, 3) == majority_element_line(lst)

def test_majority_elem_none():
    lst = [1, 2, 3, 4, 5, 6]
    assert majority_element_recursion(lst) == (None, None) == majority_element_line(lst)



