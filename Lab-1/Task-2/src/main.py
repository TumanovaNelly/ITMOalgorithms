from InsertionSort import insertion_sort_indexes

with open('../txtf/input.txt') as file:
    lst = list(map(int, file.readline().split()))

with open('../txtf/output.txt', 'w') as file: 
    print(*insertion_sort_indexes(lst), file=file)



