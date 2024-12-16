from utils import read, write


def editing_distance_memory_optimized(word1: str, word2: str) -> int:
    old_line_distance_data = [i for i in range(len(word1) + 1)]
    new_line_distance_data = [0] * (len(word1) + 1)

    for line in range(1, len(word2) + 1):
        new_line_distance_data[0] = line
        for column in range(1, len(word1) + 1):
            if word1[column - 1] == word2[line - 1]:
                new_line_distance_data[column] = old_line_distance_data[column - 1]
            else:
                new_line_distance_data[column] = 1 + min(new_line_distance_data[column - 1],
                                                          old_line_distance_data[column],
                                                          old_line_distance_data[column - 1])
        old_line_distance_data, new_line_distance_data = new_line_distance_data, old_line_distance_data

    return old_line_distance_data[-1]


def main():
    (word1, ), (word2, ) = read(type_convert=str)
    write(editing_distance_memory_optimized(word1, word2))


if __name__ == "__main__":
    main()
