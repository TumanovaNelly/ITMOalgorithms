from Lab1.Task3.src.InsertionSort import insertion_sort_reversed
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    insertion_sort_reversed(lst)
    write(*lst)


if __name__ == "__main__":
    main()


