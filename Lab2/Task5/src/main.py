from Lab2.Task5.src.MajorityElement import majority_element_recursion


def main():
    with open(r'..\txtf\input.txt') as file:
        lst = list(map(int, file.readline().split()))

    with open(r'..\txtf\output.txt', 'w') as file:
        element, number = majority_element_recursion(lst)
        print(0 if number == -1 else 1, sep=" ", file=file)


if __name__ == "__main__":
    main()
