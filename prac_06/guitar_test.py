"""Guitar Test Practical by Michael Geue"""

from prac_06.guitar import Guitar


def main():
    gibson_guitar = Guitar("Gibson L-5 CES", 1922)
    another_guitar = Guitar("Another Guitar", 2013)

    print("{} get_age() - Expected 98. Got {}".format(gibson_guitar.name, gibson_guitar.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(gibson_guitar.name, gibson_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))

    
main()
