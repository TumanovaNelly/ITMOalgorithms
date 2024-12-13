from typing import Dict, List

from utils import read, write


def count_index(string: str, beauty: Dict[str, List[str]]):
    """
    :param string: строка, обозначающая набор камней
    :param beauty: упорядоченные пары "красивых" камней: второму элементу сопоставляется список первых элементов
    :return: количество "красивых" пар в строке
    """
    counter = [0 for i in
               range(ord('a'), ord('z') + 1)]  # текущее количество раз, которое встретилось соответствующее число
    cnt = 0
    for sym in string:
        for first in beauty.get(sym, []):
            cnt += counter[ord(first) - ord('a')]
        counter[ord(sym) - ord('a')] += 1

    return cnt


def main():
    (string,), *pairs = read(type_convert=str)
    beauty = dict()
    for pair, in pairs:
        if pair[1] not in beauty:
            beauty[pair[1]] = []
        beauty[pair[1]].append(pair[0])

    write(count_index(string, beauty))


if __name__ == '__main__':
    main()
