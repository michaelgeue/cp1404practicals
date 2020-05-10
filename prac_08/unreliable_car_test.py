""""Unreliable Car Test Practical"""

from prac_08.unreliable_car import UnreliableCar


def main():
    okay_car = UnreliableCar("Okay Car", 200, 50)
    print(okay_car)
    drive_count = 0

    while okay_car.fuel != 0:
        okay_car.drive(50)
        print(okay_car)
        drive_count += 1

    print("Times driven: {}".format(drive_count))


if __name__ == '__main__':
    main()