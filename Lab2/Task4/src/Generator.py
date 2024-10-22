from random import randint

def generate(min_value, max_value, number):
    assert number > 0

    with open(r'../txtf/input.txt', 'w') as file:
        lst = [str(randint(min_value, max_value)) for _ in range(number)]
        file.write(" ".join(lst))
        file.write("\n")
        file.write(str(randint(min_value, max_value)))

if __name__ == "__main__":
    generate(-100, 100, 1000)