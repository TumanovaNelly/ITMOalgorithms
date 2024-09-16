for _ in range(3):
    a, b = map(int, input().split())

    if -(10 ** 9) <= a <= (10 ** 9) and -(10 ** 9) <= b <= (10 ** 9):
        print(a + b ** 2)
        break
    else:
        print('Incorrect numbers. Try again.')