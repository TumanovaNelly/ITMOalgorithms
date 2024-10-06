from SelectionSort import selection_sort

with open('../txtf/input.txt') as file:
    lst = list(map(int, file.readline().split()))

with open('../txtf/output.txt', 'w') as file: 
    print(*selection_sort(lst), sep="\n", file=file)
