def bin_pow(lst: list, value: int):
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = left + (right - left) // 2
        if lst[mid] < value:
            left = mid + 1
        else:
            right = mid

    if lst[right] == value:
        return right
    return -1
