def read(filename: str = r'..\txtf\input.txt', type_convert = int):
    with open(filename) as file:
        while True:
            line = list(map(type_convert, file.readline().split()))
            if line:
                yield line
            else: break


def write(*values, sep=" ", filename: str = r'..\txtf\output.txt'):
    with open(filename, 'w') as file:
        for value in values:
            print(value, end=sep, file=file)