def bin_pow(lst: list, value: int):
    lst_indexes = list(range(len(lst)))
    lst_indexes.sort(key=lambda index: lst[index])
    # индексы элементов отсортированного списка lst

    left = 0
    right = len(lst) - 1
    while left < right:
        mid = left + (right - left) // 2
        if lst[lst_indexes[mid]] < value:
            left = mid + 1
        else:
            right = mid

    if lst[lst_indexes[right]] == value:
        return lst_indexes[right]

    return -1
