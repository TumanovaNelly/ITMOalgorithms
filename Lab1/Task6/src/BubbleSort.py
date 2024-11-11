from utils import read, write


def bubble_sort(lst: list) -> None:
    for left in range(len(lst) - 1):
        flag = False
        for i in range(len(lst) - 1, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                flag = True

        if not flag: break


def main():
    lst, = read()
    bubble_sort(lst)
    write(*lst)


if __name__ == "__main__":
    main()
