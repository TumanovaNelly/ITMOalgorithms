from utils import read, write


def selection_sort_indexes(lst: list):
    for start in range(len(lst) - 1):
        mn = [lst[start], start]
        for i in range(start + 1, len(lst)):
            if lst[i] < mn[0]:
                *mn, = lst[i], i
        if start != mn[1]:
            lst[start], lst[mn[1]] = lst[mn[1]], lst[start]
            yield f"Swap elements at indices {start + 1} and {mn[1] + 1}."

    yield "No more swaps needed."


def main():
    lst, = read()
    write(*selection_sort_indexes(lst), sep="\n")


if __name__ == "__main__":
    main()