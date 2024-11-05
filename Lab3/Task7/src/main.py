from Lab3.Task7.src.RadixSort import radix_sort
from Utils.Read_n_Write import write


def main():
    with open(r"..\txtf\input.txt") as file:
        lens, number = map(int, file.readline().split())
        lst = []
        while True:
            line = file.readline()
            if line: lst.append(line)
            else: break
    write(*radix_sort(lst, lens, number))


if __name__ == "__main__":
    main()