from random import randint
from Lab3.Task4.src.SectionsAndPoints import *
from Utils.Time_Memory import time_data


def test_sections_n_points():
    sections = [(3, 5), (3, 7), (1, 4), (2, 6), (2, 3)]
    points = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    assert (list(sections_n_points(sections, points)) ==
            [0, 1, 3, 5, 4, 3, 2, 1, 0])


def test_sections_n_points_random():
    sections = []
    for _ in range(1000):
        start = randint(-1000, 1000)
        end = randint(-1000, 1000)

        if start > end:
            start, end = end, start

        sections.append((start, end))

    points = []
    for _ in range(1000):
        points.append(randint(-1000, 1000))
    points.sort()

    assert (list(sections_n_points(sections, points)) ==
            list(sections_n_points_naive(sections, points)))


def test_time():
    time = time_data(main)
    assert time < 2