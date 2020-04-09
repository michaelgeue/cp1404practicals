"""Guitars Practical by Michael Geue"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = get_guitars_list()

    max_name_length = max(len(guitar.name) for guitar in guitars)
    print(max_name_length)

    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>{}} ({}), worth $ {:10,.2f}{}".format(i + 1, guitar.name, max_name_length, guitar.year,
                                                                   guitar.cost,
                                                                   " (vintage)" if guitar.is_vintage() else ""))


def get_guitars_list():
    entering_guitars = True
    guitars = []
    while entering_guitars:
        guitar_name = input("Name: ")
        if guitar_name == "":
            entering_guitars = False
        else:
            guitar_year = get_year()
            guitar_cost = get_cost()
            guitar = Guitar(guitar_name, guitar_year, guitar_cost)
            guitars.append(guitar)
            print("{} added.".format(guitar))
    return guitars


def get_year():
    valid_input = False
    while not valid_input:
        try:
            return int(input("Year: "))
        except ValueError:
            print("Invalid entry, must be a number")


def get_cost():
    valid_input = False
    while not valid_input:
        try:
            return float(input("Cost: $ "))
        except ValueError:
            print("Invalid entry, must be a number")


main()
