from Lab2.Task5.src.MajorityElement import majority_element_recursion
from Utils.Read_n_Write import read, write


def main():
    lst, = read()
    element, number = majority_element_recursion(lst)
    write(0 if number == -1 else 1)


if __name__ == "__main__":
    main()
