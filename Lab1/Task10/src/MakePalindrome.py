from string import ascii_uppercase

from utils import read, write
from Lab1.Task1.src.InsertionSort import insertion_sort_bin_pow


def make_palindrome_general(letters_str: str) -> str:
    letters = list(letters_str)
    insertion_sort_bin_pow(letters)
  
    cur = 0
    center = str()
    palindrome_half = []
    while cur < len(letters) - 1:
        if letters[cur] == letters[cur + 1]:
            palindrome_half.append(letters[cur])
            cur += 1
        elif center == "":
            center = letters[cur]
        cur += 1

    if cur == len(letters) - 1 and center == "":
        center = letters[cur]

    return "".join(palindrome_half + [center] + list(reversed(palindrome_half)))


def make_palindrome(letters: str) -> str:
    letters_cnt = [0] * len(ascii_uppercase)

    for sym in letters:
        if sym not in ascii_uppercase:
            raise ValueError("Unknown symbol")

        letters_cnt[ord(sym) - ord("A")] += 1

    center = str()
    palindrome_half = []
    for i in range(len(letters_cnt)):
        if letters_cnt[i] % 2 == 1 and center == "":
            center = chr(ord("A") + i)

        palindrome_half.extend([chr(ord("A") + i)] * (letters_cnt[i] // 2))

    return "".join(palindrome_half + [center] + list(reversed(palindrome_half)))


def main():
    letters, = read(type_convert=str)
    write(make_palindrome(*letters))


if __name__ == "__main__":
    main()