from Lab2.Task8.src.MultPolynomials import mult_polynomials
from Utils.Read_n_Write import read, write


def main():
    f, g = read()
    write(*mult_polynomials(f, g))


if __name__ == "__main__":
    main()
