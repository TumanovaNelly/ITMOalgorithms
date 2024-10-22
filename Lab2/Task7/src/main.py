from Lab2.Task7.src.FindMaxSubarray import find_max_subarray


def main():
    with open(r'..\txtf\input.txt') as file:
        lst = list(map(int, file.readline().split()))

    with open(r'..\txtf\output.txt', 'w') as file:
        sm, start, end = find_max_subarray(lst)
        print(f"start: {start} \nend: {end} \nsum: {sm}", file=file)

if __name__ == "__main__":
    main()
