def fib(n):
    if n < 0:
        raise Exception('The number must be positive')

    last1, last2 = 0, 1
    for _ in range(n):
        last1, last2 = last2, last1 + last2

    return last1

import time
time_start = time.perf_counter()

with open('input.txt') as file:
    n = int(file.readline())

if n > 45:
    raise Exception('The number out of range')

with open('output.txt', 'w+') as file:
    file.write(str(fib(n)))

print(f'TIME {time.perf_counter() - time_start} microsec.')
