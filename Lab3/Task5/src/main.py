from Lab3.Task5.src.Hirsch import hirsch
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    write(hirsch(lst))


if __name__ == "__main__":
    main()