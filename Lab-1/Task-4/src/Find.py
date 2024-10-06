def find(lst: list, value) -> int:
    for i in range(len(lst)):
        if lst[i] == value:
            return i + 1

    return -1