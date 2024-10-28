from Lab1.Task8.src.SelectionSort import selection_sort
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    write(*selection_sort(lst), sep="\n")
    

if __name__ == "__main__":
    main()