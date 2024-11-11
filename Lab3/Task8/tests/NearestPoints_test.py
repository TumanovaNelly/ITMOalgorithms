from random import randint

from utils import time_data, memory_data
from Lab3.Task8.src.NearestPoints import quick_sort_by_norma, nearest_points_as_quick_sort, get_norma, main


def test_quick_sort_by_norma():
    for i in range(1000):
        lst = [(randint(-100, 100), randint(-100, 100)) for _ in range(100)]
        quick_sort_by_norma(lst)
        for i in range(1, len(lst)):
            assert get_norma(lst[i - 1]) <= get_norma(lst[i])


def test_nearest_points_as_quick_sort():
    for _ in range(1000):
        lst = [(randint(-100, 100), randint(-100, 100)) for _ in range(100)]
        number = randint(1, 100)
        answer = []
        nearest_points_as_quick_sort(lst, number, answer)
        mx = get_norma(sorted(lst, key=get_norma)[number - 1])
        for el in answer:
            assert get_norma(el) <= mx



def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 5
    assert peak < 5