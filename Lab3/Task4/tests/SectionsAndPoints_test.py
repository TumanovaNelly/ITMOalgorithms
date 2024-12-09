import unittest
from random import randint
from Lab3.Task4.src.SectionsAndPoints import sections_n_points, sections_n_points_naive, main
from utils import time_data, memory_data


class TestSectionsAndPoints(unittest.TestCase):
    def test_sections_n_points(self):
        # given
        sections = [(3, 5), (3, 7), (1, 4), (2, 6), (2, 3)]
        points = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_result = [0, 1, 3, 5, 4, 3, 2, 1, 0]

        # when
        result = list(sections_n_points(sections, points))

        # then
        self.assertEqual(result, expected_result)

    def test_sections_n_points_random(self):
        # given
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

        expected_result = list(sections_n_points_naive(sections, points))

        # when
        result = list(sections_n_points(sections, points))

        # then
        self.assertEqual(result, expected_result)

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
