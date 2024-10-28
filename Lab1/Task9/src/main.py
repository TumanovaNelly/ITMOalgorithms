from Lab1.Task9.src.BinAdd import bin_add
from Utils.Read_n_Write import read, write


def main():
    (first, second), = read(type_convert=str)
    first = list(map(int, list(first)))
    second = list(map(int, list(second)))
    write(*bin_add(first, second), sep="")


if __name__ == "__main__":
    main()