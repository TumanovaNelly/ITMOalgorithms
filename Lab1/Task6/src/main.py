from Lab1.Task6.src.BubbleSort import bubble_sort

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))

    bubble_sort(lst)

    with open('../txtf/output.txt', 'w') as file: 
        print(*lst, file=file)

if __name__ == "__main__":
    main()



