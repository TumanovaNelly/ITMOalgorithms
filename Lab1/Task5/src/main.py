from Lab1.Task5.src.SelectionSort import selection_sort
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    selection_sort(lst)
    write(*lst)

if __name__ == "__main__":
    main()
