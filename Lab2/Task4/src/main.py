from Lab2.Task4.src.BinPow import bin_pow
from Utils.Read_n_Write import read, write


def main():
    lst, value = read()
    write(bin_pow(lst, value[0]))


if __name__ == "__main__":
    main()
