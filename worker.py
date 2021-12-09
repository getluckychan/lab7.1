from main import Set
from sys import exit


def main():
    try:
        array = Set(int(input("Введіть розмір массиву: ")))
        array.create_list()
        return array.show_list(), array.show_summa()
    except ValueError:
        exit("введіть ціле число")

main()
