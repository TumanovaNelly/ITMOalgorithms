def bubble_sort_indexes(lst: list) -> list:
    indexes = list(range(1, len(lst) + 1))

    for left in range(len(lst) - 1):
        flag = False
        for i in range(len(lst) - 1, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                indexes[i - 1], indexes[i] = indexes[i], indexes[i - 1]
                flag = True

        if not flag: break

    return indexes

