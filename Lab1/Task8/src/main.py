from SelectionSort import selection_sort

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    with open('../txtf/output.txt', 'w') as file: 
        print(*selection_sort(lst), sep="\n", file=file)

if __name__ == "__main__":
    main()