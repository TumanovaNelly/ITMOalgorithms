from typing import List



def counting_sort(lst: List[str], indexes_lst: List[int], index: int):
    lst_copy = lst[:]
    indexes_lst_copy = indexes_lst[:]
    count = [0] * (ord('z') - ord('a') + 1)

    for word in lst:
        count[ord(word[index]) - ord('a')] += 1

    count[0] -= 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(lst_copy) - 1, -1, -1):
        sym_index = ord(lst_copy[i][index]) - ord('a')
        lst[count[sym_index]] = lst_copy[i]
        indexes_lst[count[sym_index]] = indexes_lst_copy[i]
        count[sym_index] -= 1


def radix_sort(lst: List[str], lens: int, number: int):
    indexes_lst = list(range(1, len(lst) + 1))


    for ind in range(lens - 1, lens - number - 1, -1):
        counting_sort(lst, indexes_lst, ind)
    return indexes_lst
