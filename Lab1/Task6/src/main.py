from Lab1.Task6.src.BubbleSort import bubble_sort
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    bubble_sort(lst)
    write(*lst)

if __name__ == "__main__":
    main()



