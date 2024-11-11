from typing import Tuple
import tracemalloc
import time



def read(filename: str = r'..\txtf\input.txt', type_convert: type = int):
    """
    Чтение файла построчно с преобразованием типов
    :param filename: имя файла, с которого нужно прочитать данные
    :param type_convert: все данные в файле будут конвертироваться в списки с данными этого типа
    :return: генератор списков строк
    """
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
    mode = 'w'
    if to_end:
        mode = 'a'

    with open(filename, mode) as file:
        for value in values:
            print(value, end=sep, file=file)


def time_data(func) -> float:
    """
    Запускает функцию func и возвращает время ее выполнения
    :param func: функция, время которой нужно проверить
    :return: время выполнения func
    """
    time_start = time.perf_counter()
    func()
    return time.perf_counter() - time_start


def memory_data(func) -> Tuple[float, float]:
    """
    Запускает функцию func и возвращает данные о памяти, занятой при ее выполнении
    :param func: функция, память которой нужно проверить
    :return: занятая и пиковая память соотв.
    """
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    return current / 2 ** 20, peak / 2 ** 20