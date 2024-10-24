from Lab1.Task5.src.SelectionSort import selection_sort

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    selection_sort(lst)

    with open('../txtf/output.txt', 'w') as file: 
        print(*lst, file=file)

if __name__ == "__main__":
    main()
