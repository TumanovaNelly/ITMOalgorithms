from utils import read, write


def editing_distance(word1: str, word2: str):
    word1 = " " + word1
    word2 = " " + word2
    distance_data = [[0] * len(word1) for _ in range(len(word2))]
    for i in range(len(word1)):
        distance_data[0][i] = distance_data[i][0] = i

    for line in range(1, len(word2)):
        for column in range(1, len(word1)):
            if word1[column] == word2[line]:
                distance_data[line][column] = distance_data[line - 1][column - 1]
            else:
                distance_data[line][column] = 1 + min(distance_data[line][column - 1],
                                                      distance_data[line - 1][column - 1],
                                                      distance_data[line - 1][column])

    actions = []
    line = len(word2) - 1
    column = len(word1) - 1
    while line >= 0 and column >= 0:
        if word1[column] != word2[line]:
            if distance_data[line][column - 1] == distance_data[line][column] - 1:
                actions.append(f"del {word1[column]}")
                line += 1
            elif distance_data[line - 1][column - 1] == distance_data[line][column] - 1:
                actions.append(f"change {word1[column]} {word2[line]}")
            elif distance_data[line - 1][column] == distance_data[line][column] - 1:
                actions.append(f"add {word2[line]}")
                column += 1
        line -= 1
        column -= 1
    return reversed(actions)




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
    print(*editing_distance(word1, word2), sep='\n')


if __name__ == "__main__":
    main()
