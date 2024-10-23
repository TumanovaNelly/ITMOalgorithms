from random import randint


def generate(min_value: int, max_value: int, number: int):
    assert number > 0

    with open(r'../txtf/input.txt', 'w') as file:
        lst = [str(randint(min_value, max_value)) for _ in range(number)]
        file.write(" ".join(lst))


if __name__ == "__main__":
    generate(0, 1, 1001)