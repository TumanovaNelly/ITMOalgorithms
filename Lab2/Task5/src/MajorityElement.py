import typing as tp


def majority_element_recursion(lst: tp.List[int], start: int = 0, end: int = -1) -> tp.Tuple[tp.Optional[int], int]:
    """
    Поиск мажорирующего элемента на части lst от start до end (не включительно)
    :param lst: список
    :param start: начальный индекс списка
    :param end: конечный индекс (end = len(lst) <-> end == -1)
    :return: значение мажорирующего элемента (None, если его нет) и
    количество раз, которое он встречается в списке (-1, если его нет)
    """

    if end == -1:
        end = len(lst)

    num_elements = end - start
    if num_elements == 0:
        return None, -1
    if num_elements == 1:
        return lst[start], 1

    mid = start + num_elements // 2
    majority_left, num_left = majority_element_recursion(lst, start, mid)
    majority_right, num_right = majority_element_recursion(lst, mid, end)

    if num_left != -1:
        for i in range(mid, end):
            if lst[i] == majority_left:
                num_left += 1
        if num_left > num_elements // 2:
            return majority_left, num_left

    if num_right != -1:
        for i in range(start, mid):
            if lst[i] == majority_right:
                num_right += 1
        if num_right > num_elements // 2:
            return majority_right, num_right

    return None, -1


def majority_element_line(lst: tp.List[int]) -> tp.Tuple[tp.Optional[int], int]:
    """
    Поиск мажорирующего элемента в lst за линию
    :param lst: список
    :return: значение мажорирующего элемента (None, если его нет) и
    количество раз, которое он встречается в списке (-1, если его нет)
    """

    num_without_pair = 0 # количество элементов которые пока без пары
    candidate = None # Значение элементов без пары
    """
    Предположим, что мажорирующий элемент есть.
    Будем объединять разные элементы в пары. Т.к в списке есть элемент, который входит в список 
    больше n // 2 раз, всех на подобные пары разбить не получится: без пары останутся
    мажорирующие элементы
    """
    for elem in lst:
        if num_without_pair == 0:
            candidate = elem
            num_without_pair += 1
        elif elem == candidate:
            num_without_pair += 1
        else:
            num_without_pair -= 1

    """
    Проверяем, действительно ли кандидат (оставшийся без пары) мажорирует
    """
    cnt = 0
    for elem in lst:
        if elem == candidate:
            cnt += 1

    return (candidate, cnt) if cnt > len(lst) // 2 else (None, -1)




