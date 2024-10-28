from Lab1.Task2.src.InsertionSort import insertion_sort_indexes_bin_pow
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    write(*insertion_sort_indexes_bin_pow(lst))


if __name__ == "__main__":
    main()


