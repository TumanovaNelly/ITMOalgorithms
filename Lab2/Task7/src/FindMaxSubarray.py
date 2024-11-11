import typing as tp
from Utils.Read_n_Write import read, write


def find_max_subarray(lst: tp.List[int]) -> tp.Tuple[int, int, int]:
    max_subarray = lst[0] # сумма элементов максимального подмассива
    left, right = 0, 1 # границы максимального подмассива


    sm = 0 # сумма подмассива от 0 до текущего индекса
    min_sm = min_sm_len = 0 # подмассив от 0 до min_sm_len с минимальной суммой
    for ind, elem in enumerate(lst):
        sm += elem
        if max_subarray < sm - min_sm:
            max_subarray = sm - min_sm
            left = min_sm_len
            right = ind + 1

        if min_sm > sm:
            min_sm = sm
            min_sm_len = ind + 1

    return max_subarray, left, right


#______________________________________________
def find_max_subarray_naive(lst: tp.List[int]) -> tp.Tuple[int, int, int]:
    max_subarray = lst[0]
    left = 0
    right = 1
    for l in range(len(lst)):
        for r in range(l + 1, len(lst) + 1):
            sm = 0
            for i in range(l, r):
                sm += lst[i]
            if max_subarray < sm:
                max_subarray = sm
                left, right = l, r

    return max_subarray, left, right


def main():
    lst, = read()
    sm, start, end = find_max_subarray(lst)
    write(f"start: {start}", f"end: {end}", f"sum: {sm}", sep="\n")


if __name__ == "__main__":
    main()


