from random import shuffle
from Utils.Read_n_Write import write


def generate(number: int):
    assert number > 0
    lst = list(map(str, range(number)))
    shuffle(lst)
    write(*lst, filename=r'../txtf/input.txt')


if __name__ == "__main__":
    generate(1000)