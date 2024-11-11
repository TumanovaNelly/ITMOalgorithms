from typing import TypeVar
from Lab4.Task13.src.List import List
from Utils.Read_n_Write import read, write

T = TypeVar('T')


class Queue:
    def __init__(self):
        self.queue = List()


    def push(self, item: T) -> None:
        self.queue.push_back(item)


    def pop(self) -> T:
        return self.queue.pop_front()


def main():
    queue = Queue()
    write()
    for line in read(type_convert=str):
        if line[0] == '+':
            queue.push(line[1])
        else:
            write(queue.pop(), sep="\n", to_end=True)



if __name__ == '__main__':
    main()
