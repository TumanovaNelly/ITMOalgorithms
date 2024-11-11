from collections.abc import Iterator
from typing import List, Tuple
from Lab3.Task1.src.QuickSort import quick_sort
from Utils.Read_n_Write import read, write


# флаги
START = 0
POINT = 1
END = 2


# Алгоритм выводит ответы соответственно для точек, отсортированных в возрастающем порядке
def sections_n_points(sections: List[Tuple[int, int]], points: List[int]) -> Iterator[int]:
    all_points = []

    for section in sections:
        all_points.append((section[0], START))
        all_points.append((section[1], END))

    for point in points:
        all_points.append((point, POINT))

    quick_sort(all_points)
    active = 0
    for point in all_points:
        if point[1] == START:
            active += 1
        elif point[1] == POINT:
            yield active
        else: active -= 1


#-------------------------------------------------

def sections_n_points_naive(sections: List[Tuple[int, int]], points: List[int]) -> Iterator[int]:
    for point in points:
        cnt = 0

        for start, end in sections:
            if start <= point <= end:
                cnt += 1

        yield cnt


def main():
    *sections, points = read()
    write(*sections_n_points(sections, points))

if __name__ == "__main__":
    main()