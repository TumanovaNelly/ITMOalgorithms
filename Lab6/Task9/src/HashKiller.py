from itertools import product
from typing import Tuple

from utils import read, write

INT_BITS_NUMBER = 32
MASK = (1 << INT_BITS_NUMBER) - 1  # == 0b111...111 (NUMBER_IN_MT_SEQ единицы в двоичной записи)


def find_number_in_Morse_Thue_sequence():
    number = 1
    while (number * (number - 1)) // 2 < INT_BITS_NUMBER:
        number += 1
    return number - 2


NUMBER_IN_MT_SEQ = find_number_in_Morse_Thue_sequence()  # порядковый номер строки из последовательности Морса-Туэ


def get_hash(string: str, mult: int):
    hsh = 0
    for sym in string:
        hsh = (hsh * mult + ord(sym)) & MASK  # <& MASK> эквивалентно взятию числа по модулю 2^32
    return hsh


def generate_odd_killers(null_sym='A', one_sym='B') -> Tuple[str, str]:
    """
    :param null_sym: символ генерируемой строки
    :param one_sym: символ генерируемой строки
    :return: NUMBER_IN_MT_SEQ из последовательности Морса-Туэ и ее инверсия соответственно
    """
    number = NUMBER_IN_MT_SEQ
    number = 1 << number  # 2^number
    string = [null_sym] * number
    not_string = [one_sym] * number
    length = 1
    while length < number:
        for i in range(length):
            if string[i] == null_sym:
                string[length + i] = one_sym
                not_string[length + i] = null_sym
        length *= 2

    return ''.join(string), ''.join(not_string)


def generate_even_killer(sym='A'):
    return sym * INT_BITS_NUMBER


def find_power_of_two(number: int):
    """
    :param number: число N
    :return: степень двойки S, такая, что N <= 2^S
    """
    return (number - 1).bit_length()


def generate_strings(number: int):
    if number == 1:
        yield 'A'
        return
    cnt = 0
    even_killer = generate_even_killer()
    for model in product([*generate_odd_killers()], repeat=find_power_of_two(number)):
        if cnt >= number: break
        cnt += 1
        yield "".join(model) + even_killer


def main():
    (number,), = read()
    write(*generate_strings(number), sep="\n")


if __name__ == '__main__':
    main()
