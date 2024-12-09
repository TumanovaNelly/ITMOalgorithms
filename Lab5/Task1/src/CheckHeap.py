from typing import Optional


def get_parent_index(element_index: int) -> Optional[int]:
    return (element_index + 1) // 2 - 1 if element_index > 0 else None

def check_heap(candidate: list) -> bool:
    for i in range(1, len(candidate)):
        if candidate[get_parent_index(i)] > candidate[i]:
            return False
    return True


if __name__ == "__main__":
    print(check_heap([1, 0, 1, 2, 0]))
    print(check_heap([1, 3, 2, 5, 4]))