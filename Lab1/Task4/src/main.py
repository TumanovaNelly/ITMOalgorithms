from Lab1.Task4.src.Find import find
from Utils.Read_n_Write import read, write


def main():
    lst, value = read()
    write(*find(lst, value[0]))


if __name__ == "__main__":
    main()