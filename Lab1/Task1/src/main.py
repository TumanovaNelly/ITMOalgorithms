from Lab1.Task1.src.InsertionSort import insertion_sort_bin_pow
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    insertion_sort_bin_pow(lst)
    write(*lst)

if __name__ == "__main__":
    main()




