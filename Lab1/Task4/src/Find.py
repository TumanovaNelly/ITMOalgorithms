from utils import read, write


def find(lst: list, value) -> list:
    indexes = []
    for i in range(len(lst)):
        if lst[i] == value:
            indexes.append(i + 1)
    
    if not indexes:
        indexes.append(-1)
    return indexes


def main():
    lst, (value, ) = read()
    write(*find(lst, value), sep=", ")


if __name__ == "__main__":
    main()