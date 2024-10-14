from Lab1.Task3.src.InsertionSort import insertion_sort_reversed

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    insertion_sort_reversed(lst)

    with open('../txtf/output.txt', 'w') as file: 
        print(*lst, file=file)

if __name__ == "__main__":
    main()


