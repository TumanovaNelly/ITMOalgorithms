from random import shuffle

def generate(number):
    assert number > 0

    with open(r'../txtf/input.txt', 'w') as file:
        lst = list(map(str, range(number)))
        shuffle(lst)
        file.write(" ".join(lst))

if __name__ == "__main__":
    generate(1000)