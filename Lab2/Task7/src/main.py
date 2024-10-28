from Lab2.Task7.src.FindMaxSubarray import find_max_subarray
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    sm, start, end = find_max_subarray(lst)
    write(f"start: {start}", f"end: {end}", f"sum: {sm}", sep="\n")


if __name__ == "__main__":
    main()
