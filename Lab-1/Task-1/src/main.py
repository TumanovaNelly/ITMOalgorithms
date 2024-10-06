from InsertionSort import insertion_sort

with open('../txtf/input.txt') as file:
    lst = list(map(int, file.readline().split()))

insertion_sort(lst)

with open('../txtf/output.txt', 'w') as file: 
    print(*lst, file=file)




