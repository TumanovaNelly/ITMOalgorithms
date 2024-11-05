from Lab3.Task8.src.NearestPoints import nearest_points
from Utils.Read_n_Write import read, write


def main():
    number, *lst = read()
    write(*nearest_points(lst, *number))


if __name__ == "__main__":
    main()