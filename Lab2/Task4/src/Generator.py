from random import randint
from Utils.Read_n_Write import write


def generate(min_value: int, max_value: int, number: int):
    assert number > 0
    lst = [str(randint(min_value, max_value)) for _ in range(number)]
    write(*lst, "\n" + str(randint(min_value, max_value)),
          filename=r'../txtf/input.txt')


if __name__ == "__main__":
    generate(-100, 100, 1000)