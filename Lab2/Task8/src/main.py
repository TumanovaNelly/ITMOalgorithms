from Lab2.Task8.src.MultPolynomials import mult_polynomials


def main():
    with open(r'..\txtf\input.txt') as file:
        f = list(map(int, file.readline().split()))
        g = list(map(int, file.readline().split()))

    with open(r'..\txtf\output.txt', 'w') as file:
        print(*mult_polynomials(f, g), sep=" ", file=file)


if __name__ == "__main__":
    main()
