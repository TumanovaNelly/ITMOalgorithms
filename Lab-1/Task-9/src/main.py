from BinAdd import bin_add

with open('../txtf/input.txt') as file:
    first, second = map(list, file.readline().split())
    first = list(map(int, first))
    second = list(map(int, second))

with open('../txtf/output.txt', 'w') as file: 
    print(*bin_add(first, second), sep="", file=file)
