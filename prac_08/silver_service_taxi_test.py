""""Silver Service Taxi Test Practical"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi('Hummer', 100, 4)
    print(hummer)

    limo = SilverServiceTaxi('Limo', 100, 2)
    print(limo)
    limo.drive(18)
    print(limo)
    print("Current Fare: ${:.2f}".format(limo.get_fare()))


if __name__ == '__main__':
    main()
