import unittest
from random import randint

from utils import time_data, memory_data
from Lab3.Task8.src.NearestPoints import quick_sort_by_norma, nearest_points_as_quick_sort, get_norma, main


class TestNearestPoints(unittest.TestCase):
    def test_quick_sort_by_norma(self):
        for i in range(1000):
            # given
            lst = [(randint(-100, 100), randint(-100, 100)) for _ in range(100)]

            # when
            quick_sort_by_norma(lst)

            # then
            for i in range(1, len(lst)):
                self.assertLessEqual(get_norma(lst[i - 1]), get_norma(lst[i]))

    def test_nearest_points_as_quick_sort(self):
        for i in range(1000):
            # given
            lst_points = [(randint(-100, 100), randint(-100, 100)) for _ in range(100)]
            points_number = randint(1, 100)
            result = []
            mx_norma_in_expected_result = get_norma(sorted(lst_points, key=get_norma)[points_number - 1])

            # when
            nearest_points_as_quick_sort(lst_points, points_number, result)

            # then
            for el in result:
                self.assertLessEqual(get_norma(el), mx_norma_in_expected_result)

    def test_time(self):
        # when
        time = time_data(main)

        # then
        self.assertLess(time, 2)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)

        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == '__main__':
    unittest.main()
