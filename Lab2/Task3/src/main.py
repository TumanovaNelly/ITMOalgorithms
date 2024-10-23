from Lab2.Task3.src.CountInversions import merge_sort_count_inversions


def main():
    with open(r'..\txtf\input.txt') as file:
        lst = list(map(int, file.readline().split()))

    with open(r'..\txtf\output.txt', 'w') as file:
        print(merge_sort_count_inversions(lst), file=file)


if __name__ == "__main__":
    main()
