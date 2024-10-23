from Lab2.Task4.src.BinPow import bin_pow


def main():
    with open(r'..\txtf\input.txt') as file:
        lst = list(map(int, file.readline().split()))
        value = int(file.readline())

    with open(r'..\txtf\output.txt', 'w') as file:
        print(bin_pow(lst, value), sep=" ", file=file)


if __name__ == "__main__":
    main()
