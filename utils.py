from typing import Tuple
import tracemalloc
import time
from inspect import stack
from os.path import abspath, dirname


def get_calling_file_path():
    file_path = stack()[2].filename
    return abspath(file_path)


def read(filename: str = r'..\txtf\input.txt', type_convert: type = int):
    """
    Чтение файла построчно с преобразованием типов
    :param filename: имя файла, с которого нужно прочитать данные
    :param type_convert: все данные в файле будут конвертироваться в списки с данными этого типа
    :return: генератор списков строк
    """
    filename = fr'{dirname(get_calling_file_path())}\{filename}'

    with open(filename) as file:
        while True:
            line = file.readline().split()
            if not line: break

            if type_convert != str:
                line = list(map(type_convert, line))

            yield line


def write(*values, sep: str = " ", filename: str = r'..\txtf\output.txt', to_end: bool = False) -> None:
    """
    Запись в файл списка values
    :param values: данные, которые необходимо записать
    :param sep: разделитель данных
    :param filename: имя файла, куда будут записываться данные
    :param to_end: определяет, будет ли перезаписан файл или данные будут записаны в конец файла
    """
    filename = fr'{dirname(get_calling_file_path())}\{filename}'

    mode = 'w'
    if to_end:
        mode = 'a'

    with open(filename, mode) as file:
        print(*values, sep=sep, file=file)


def time_data(func) -> float:
    """
    Запускает функцию func и возвращает время ее выполнения в секундах
    :param func: функция, время которой нужно проверить
    :return: время выполнения func
    """
    time_start = time.perf_counter()
    func()
    return time.perf_counter() - time_start


def memory_data(func) -> Tuple[float, float]:
    """
    Запускает функцию func и возвращает данные о памяти, занятой при ее выполнении, в Mб
    :param func: функция, память которой нужно проверить
    :return: занятая и пиковая память соотв.
    """
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    return current / 2 ** 20, peak / 2 ** 20