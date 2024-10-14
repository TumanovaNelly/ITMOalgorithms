from Lab1.Task2.src.InsertionSort import insertion_sort_indexes_bin_pow

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    with open('../txtf/output.txt', 'w') as file: 
        print(*insertion_sort_indexes_bin_pow(lst), file=file)


if __name__ == "__main__":
    main()


