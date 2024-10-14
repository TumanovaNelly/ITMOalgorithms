with open('../txtf/input.txt') as file:
    a, b = map(int, file.readline().split())

if -(10 ** 9) <= a <= (10 ** 9) and -(10 ** 9) <= b <= (10 ** 9):
    with open('../txtf/output.txt', 'w+') as file:
        file.write(str(a + b ** 2))
else:
    print('Incorrect numbers. Try again.')