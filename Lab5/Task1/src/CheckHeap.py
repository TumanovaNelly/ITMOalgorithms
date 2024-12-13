from typing import Optional

from utils import read, write


def get_parent_index(element_index: int) -> Optional[int]:
    return (element_index + 1) // 2 - 1 if element_index > 0 else None


def check_heap(candidate: list) -> bool:
    for i in range(1, len(candidate)):
        if candidate[get_parent_index(i)] > candidate[i]:
            return False
    return True


def main():
    data, = read()
    write("YES" if check_heap(data) else "NO")


if __name__ == "__main__":
    main()
