from random import randint
from Utils.Read_n_Write import write


def generate(min_value: int, max_value: int, number: int):
    assert number > 0
    lst = [str(randint(min_value, max_value)) for _ in range(number)]
    write(*lst, filename=r'..\txtf\input.txt')


if __name__ == "__main__":
    generate(-10 ** 8, 10 ** 8, 1000)