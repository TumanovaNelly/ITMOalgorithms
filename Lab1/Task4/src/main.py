from Find import find

def main():
    with open('../txtf/input.txt') as file:
        lst = list(map(int, file.readline().split()))
        value = int(file.readline())

    with open('../txtf/output.txt', 'w') as file: 
        print(*find(lst, value), file=file)


if __name__ == "__main__":
    main()