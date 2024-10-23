from random import randint


def generate(min_value: int, max_value: int, number: int):
    assert number > 0

    with open(r'../txtf/input.txt', 'w') as file:
        f = [str(randint(min_value, max_value)) for _ in range(number)]
        file.write(" ".join(f))
        file.write("\n")
        f = [str(randint(min_value, max_value)) for _ in range(number)]
        file.write(" ".join(f))


if __name__ == "__main__":
    generate(-10 ** 8, 10 ** 8, 1000)