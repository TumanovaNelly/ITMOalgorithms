import typing as tp
from Utils.Read_n_Write import read, write


def merge(list1: tp.List[int], list2: tp.List[int], target: tp.List[int], start_index: int = 0) -> None:
    cur1 = cur2 = 0
    cur_target = start_index

    while cur1 < len(list1) and cur2 < len(list2):
        if list1[cur1] <= list2[cur2]:
            target[cur_target] = list1[cur1]
            cur1 += 1
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


def merge_sort(lst: tp.List[int]) -> None:
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


def main():
    lst, = read()
    merge_sort(lst)
    write(*lst)


if __name__ == "__main__":
    main()



