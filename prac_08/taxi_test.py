""""Taxi Test Practical"""

from prac_08.taxi import Taxi


def main():
    prius_1 = Taxi('Prius 1', 100)
    prius_1.drive(40)
    print(prius_1)
    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1)


if __name__ == '__main__':
    main()
