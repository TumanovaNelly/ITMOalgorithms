from Lab3.Task1.src.QuickSort import quick_sort
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    quick_sort(lst)
    write(*lst)


if __name__ == "__main__":
    main()