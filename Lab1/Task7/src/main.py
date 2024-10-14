from Lab1.Task7.src.BubbleSort import bubble_sort_indexes

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))
        if len(lst) % 2 == 0:
            raise ValueError("The list must contain an odd number of elements")

    indexes = bubble_sort_indexes(lst)

    with open('../txtf/output.txt', 'w') as file: 
        print(indexes[0],  indexes[len(indexes) // 2], indexes[-1], sep=" ", file=file)

if __name__ == "__main__":
    main()

