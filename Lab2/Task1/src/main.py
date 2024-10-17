from Lab2.Task1.src.MergeSort import merge_sort

def main():
    with open(r'..\txtf\input.txt') as file:
        lst = list(map(int, file.readline().split()))

    merge_sort(lst)

    with open(r'..\txtf\output.txt', 'w') as file:
        print(*lst, sep=" ", file=file)

if __name__ == "__main__":
    main()
