import typing as tp


def merge(list1: tp.List[int], list2: tp.List[int], target: tp.List[int], start_index: int = 0) -> None:
    """
    Слияние list1 и list2 в target, начиная с индекса target = start
    :param list1: отсортированный список 1
    :param list2: отсортированный список 2
    :param target: список, в который будет помещён результат слияния списка 1 и списка 2
    :param start_index: индекс в списке target, откуда начнётся запись элементов
    """
    cur1 = cur2 = 0   # текущие индексы в list1 и list2 соотв.
    cur_target = start_index # текущий индекс в target

    """
    Проходимся по спискам, пока один из них не закончится
    """
    while cur1 < len(list1) and cur2 < len(list2):
        """
        На каждой итерации сравниваются текущие элементы list1[cur1] и list2[cur2]. 
        Меньший из них из списка list_i добавляется в target
        Следующий элемент списка list_i становится текущим 
        """
        if list1[cur1] <= list2[cur2]:
            target[cur_target] = list1[cur1]
            cur1 += 1
        else:
            target[cur_target] = list2[cur2]
            cur2 += 1
        cur_target += 1

    """
    Если первым закончился первый список, записываем остатки второго в target, если второй - первого 
    """
    if cur1 == len(list1):
        for i in range(cur2, len(list2)):
            target[cur_target] = list2[i]
            cur_target += 1
    else:
        for i in range(cur1, len(list1)):
            target[cur_target] = list1[i]
            cur_target += 1


def merge_sort(lst: tp.List[int]) -> None:
    """
    Сортировка списка слиянием на месте
    :param lst: список, который нужно отсортировать
    """

    """
    Разделим список на подсписки длиной 1, будем попарно их сливать
    Список преобр. в список отсортированных подсписков длиной 2 (мб кроме последнего), 
                    будем попарно сливать эти подсписки (если их нечетное количество, оставляем последний как есть)
    Список преобр. в список отсортированных подсписков длиной 4 (мб кроме последнего), 
                    будем попарно сливать эти подсписки (если их нечетное количество, оставляем последний как есть)
    ..........
    Список преобр. в список отсортированных подсписков длиной len(списка) // 2 (мб кроме последнего), 
                    будем попарно сливать эти подсписки (если их нечетное количество, оставляем последний как есть)
    Делаем это упражнение, пока подсписки не достигнут длины len(списка)
    """
    len_merging_lists = 1 # длина сливающихся подсписков
    while len_merging_lists < len(lst):
        start_index = 0  # начальный индекс пары сливающихся подсписков
        while start_index + len_merging_lists < len(lst):
            if lst[start_index + len_merging_lists - 1] <= lst[start_index + len_merging_lists]:
                start_index += 2 * len_merging_lists
                continue

            merge(lst[start_index : start_index + len_merging_lists],
                  lst[start_index + len_merging_lists : min(len(lst), start_index + 2 * len_merging_lists)],
                  lst, start_index)

            start_index += 2 * len_merging_lists
        len_merging_lists *= 2





