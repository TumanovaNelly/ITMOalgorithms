from Find import find

with open('../txtf/input.txt') as file:
    lst = list(map(int, file.readline().split()))
    value = int(file.readline())

with open('../txtf/output.txt', 'w') as file: 
    print(find(lst, value), file=file)
