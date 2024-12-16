from utils import read, write


def is_match(string: str, pattern: str) -> bool:
    string = " " + string
    pattern = " " + pattern
    is_match_data = [[False] * len(string) for _ in range(len(pattern))]
    is_match_data[0][0] = True
    line = 1
    while line < len(pattern) and pattern[line] == '*':
        is_match_data[line][0] = True
        line += 1

    for line in range(1, len(pattern)):
        for column in range(1, len(string)):
            if pattern[line] == '*':
                is_match_data[line][column] = is_match_data[line - 1][column] or is_match_data[line][column - 1]
            else:
                is_match_data[line][column] = (is_match_data[line - 1][column - 1] and
                                               (pattern[line] == '?' or pattern[line] == string[column]))

    return is_match_data[-1][-1]


def is_match_memory_optimized(string: str, pattern: str) -> bool:
    old_line_is_match_data = [False] * (len(string) + 1)
    old_line_is_match_data[0] = True
    new_line_is_match_data = [False] * (len(string) + 1)

    is_start = True
    for line in range(len(pattern)):
        new_line_is_match_data[0] = False
        if is_start:
            if pattern[line] == '*':
                new_line_is_match_data[0] = True
            else:
                is_start = False

        for column in range(1, len(string) + 1):
            if pattern[line] == '*':
                new_line_is_match_data[column] = new_line_is_match_data[column - 1] or old_line_is_match_data[column]
            else:
                new_line_is_match_data[column] = (old_line_is_match_data[column - 1] and
                                                  (pattern[line] == '?' or pattern[line] == string[column - 1]))

        old_line_is_match_data, new_line_is_match_data = new_line_is_match_data, old_line_is_match_data

    return old_line_is_match_data[-1]


def main():
    (pattern, ), (string, ) = read(type_convert=str)
    write('YES' if is_match_memory_optimized(string, pattern) else 'NO')


if __name__ == '__main__':
    main()
