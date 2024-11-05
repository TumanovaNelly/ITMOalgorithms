from Lab3.Task3.src.ScarecrowSort import scarecrow_sort_real_sorting
from Utils.Read_n_Write import read, write


def main():
    delta, lst = read()
    if scarecrow_sort_real_sorting(lst, *delta):
        write("YES")
    else: write("NO")


if __name__ == "__main__":
    main()