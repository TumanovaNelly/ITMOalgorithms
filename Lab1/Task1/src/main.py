from InsertionSort import insertion_sort_bin_pow

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    insertion_sort_bin_pow(lst)

    with open('../txtf/output.txt', 'w') as file: 
        print(*lst, file=file)

if __name__ == "__main__":
    main()




