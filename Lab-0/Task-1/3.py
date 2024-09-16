with open('input.txt') as file:
    a, b = map(int, file.readline().split())

if -(10 ** 9) <= a <= (10 ** 9) and -(10 ** 9) <= b <= (10 ** 9):
    with open('output.txt', 'w+') as file:
        file.write(str(a + b))
else:
    print('Incorrect numbers. Try again.')
