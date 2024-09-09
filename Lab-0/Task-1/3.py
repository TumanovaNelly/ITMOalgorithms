with open(r'C:\Users\Admin\Desktop\PersonalPapka\ITMOlabs\Algorithms\Lab-0\Task-1\input.txt', 'r+') as file:
    a, b = list(map(int, file.readline().split()))

if a < -(10 ** 9) or a > 10 ** 9 or b < -(10 ** 9) or b > 10 ** 9:
    raise Exception('The number out of range')

with open(r'C:\Users\Admin\Desktop\PersonalPapka\ITMOlabs\Algorithms\Lab-0\Task-1\output.txt', 'w+') as file:
    file.write(str(a + b))
