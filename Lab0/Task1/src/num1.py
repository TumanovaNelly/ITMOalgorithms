for _ in range(3):
    a, b = map(int, input('Enter 2 numbers: ').split())

    if -(10 ** 9) <= a <= (10 ** 9) and -(10 ** 9) <= b <= (10 ** 9):
        print(f'{a} + {b} = {a + b}')
        break
    else: print('Incorrect numbers. Try again.')