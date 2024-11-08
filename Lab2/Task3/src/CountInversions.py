import typing as tp
from Utils.Read_n_Write import *


def merge_count_inversions(list1: tp.List[int], list2: tp.List[int], target: tp.List[int], start_index: int = 0) -> int:
    cnt = 0
    cur1 = cur2 = 0   # текущие индексы в list1 и list2 соотв.
    cur_target = start_index # текущий индекс в target
    while cur1 < len(list1) and cur2 < len(list2):
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
        cnt += (len(list1) - cur1) * len(list2)

    return cnt


def merge_sort_count_inversions(lst: list) -> int:
    count_inv = 0 # счетчик инверсий
    len_merging_lists = 1 # длина сливающихся подсписков
    while len_merging_lists < len(lst):
        start_index = 0  # начальный индекс пары сливающихся подсписков
        while start_index + len_merging_lists < len(lst):
            if lst[start_index + len_merging_lists - 1] <= lst[start_index + len_merging_lists]:
                start_index += 2 * len_merging_lists
                continue

            count_inv += merge_count_inversions(lst[start_index : start_index + len_merging_lists],
                  lst[start_index + len_merging_lists : min(len(lst), start_index + 2 * len_merging_lists)],
                  lst, start_index)

            start_index += 2 * len_merging_lists
        len_merging_lists *= 2

    return count_inv


#______________________________________________
def count_inversions_naive(lst: tp.List[int]) -> int:
    cnt = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                cnt += 1

    return cnt


def main():
    lst, = read()
    write(merge_sort_count_inversions(lst))


if __name__ == "__main__":
    main()



