from Lab3.Task4.src.SectionsAndPoints import sections_n_points
from Utils.Read_n_Write import read, write


def main():
    *sections, points = read()
    write(*sections_n_points(sections, points))

if __name__ == "__main__":
    main()