a, b = map(int, input().split())

if a < -(10 ** 9) or a > 10 ** 9 or b < -(10 ** 9) or b > 10 ** 9:
    raise Exception('The number out of range')

print(a + b)