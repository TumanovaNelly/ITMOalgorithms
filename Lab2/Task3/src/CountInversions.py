def merge_count_inversions(list1: list, list2: list, target: list, start_index: int = 0) -> int:
    cnt = 0
    """
    Для каждого элемента из левого списка считаем количество меньших элементов из правого списка
    """
    cur1 = cur2 = 0   # текущие индексы в list1 и list2 соотв.
    cur_target = start_index # текущий индекс в target
    while cur1 < len(list1) and cur2 < len(list2):
        """
        Если текущий элемент левого списка оказался меньше текущего правого, значит,
        все элементы, меньшие текущего правого, меньше текущего левого, 
        иначе на предыдущей итерации взяли бы текущий левый
        """
        if list1[cur1] <= list2[cur2]:
            target[cur_target] = list1[cur1]
            cur1 += 1
            cnt += cur2
        else:
            target[cur_target] = list2[cur2]
            cur2 += 1
        cur_target += 1


    if cur1 == len(list1):
        for i in range(cur2, len(list2)):
            target[cur_target] = list2[i]
            cur_target += 1
    else:
        for i in range(cur1, len(list1)):
            target[cur_target] = list1[i]
            cur_target += 1
        """
        Если первым закончился второй список, для каждого оставшегося элемента
        в левом списке все элементы из правого списка меньше него
        (к результату прибавляется len(list2) для каждого оставшегося в первом списке)
        """
        cnt += (len(list1) - cur1) * len(list2)

    return cnt


def merge_sort_count_inversions(lst: list) -> int:
    """
    :param lst: список, который нужно отсортировать
    :return: None: сортировка на месте
    """
    count_inv = 0 # счетчик инверсий
    len_merging_lists = 1 # длина сливающихся подсписков
    while len_merging_lists < len(lst):
        start_index = 0  # начальный индекс пары сливающихся подсписков
        while start_index + len_merging_lists < len(lst):
            if lst[start_index + len_merging_lists - 1] <= lst[start_index + len_merging_lists]:
                start_index += 2 * len_merging_lists
                continue

            """
            Количество инверсий для левого и правого списков отдельно уже посчитаны. 
            Объединим списки. Чтобы посчитать количество инверсий, надо для каждого элемента узнать, 
            сколько элементов меньше него стоит правее
            Для каждого элемента из правой части мы знаем сколько элементов из правой части меньше него стоит правее
            (количество инверсий для правой части)
            Для каждого элемента из левой части мы знаем сколько элементов из левой части меньше него стоит правее, 
            но не знаем, сколько элементов из правой части меньше него стоит правее 
            Для каждого числа из левой части будем искать количество элементов из правой части, которые меньше него, 
            и прибавлять это значение к общему количеству инверсий
            """
            count_inv += merge_count_inversions(lst[start_index : start_index + len_merging_lists],
                  lst[start_index + len_merging_lists : min(len(lst), start_index + 2 * len_merging_lists)],
                  lst, start_index)

            start_index += 2 * len_merging_lists
        len_merging_lists *= 2

    return count_inv

#______________________________________________
def count_inversions_naive(lst: list):
    cnt = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                cnt += 1

    return cnt



