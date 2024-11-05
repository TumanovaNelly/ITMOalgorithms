from typing import List, Tuple

def nearest_points(lst: List[Tuple[int, int]], number: int):
    return sorted(lst, key=lambda x: x[0] ** 2 + x[1] ** 2)[:number]