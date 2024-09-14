with open('input.txt', 'r+') as file:
    a, b = map(int, file.readline().split())

if a < -(10 ** 9) or a > 10 ** 9 or b < -(10 ** 9) or b > 10 ** 9:
    raise Exception('The number out of range')

with open('output.txt', 'w+') as file:
    file.write(str(a + b ** 2))