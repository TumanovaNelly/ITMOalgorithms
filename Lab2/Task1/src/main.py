from Lab2.Task1.src.MergeSort import merge_sort
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    merge_sort(lst)
    write(*lst)


if __name__ == "__main__":
    main()