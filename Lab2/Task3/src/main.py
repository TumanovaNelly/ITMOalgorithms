from Lab2.Task3.src.CountInversions import merge_sort_count_inversions
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    write(merge_sort_count_inversions(lst))


if __name__ == "__main__":
    main()
