def selection_sort(lst: list) -> None:
    for start in range(len(lst) - 1):
        mn = [lst[start], start]
        for i in range(start + 1, len(lst)):
            if lst[i] < mn[0]:
                *mn, = lst[i], i
        lst[start], lst[mn[1]] = lst[mn[1]], lst[start]