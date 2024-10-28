from Lab1.Task7.src.BubbleSort import bubble_sort_indexes
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    if len(lst) % 2 == 0:
        raise ValueError("The list must contain an odd number of elements")

    indexes = bubble_sort_indexes(lst)
    write(indexes[0],  indexes[len(indexes) // 2], indexes[-1])


if __name__ == "__main__":
    main()

