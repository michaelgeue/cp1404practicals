"""Taxi Simulator Practical"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

Taxi.price_per_km = 1.20  # Updated price to match sample output but keep other test files at original price of 1.23
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    total_cost = 0
    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = get_taxi_choice()
        elif menu_choice == "d":
            if not current_taxi:
                print("No taxi selected")
            else:
                total_cost += drive_taxi(current_taxi)
        else:
            print("Invalid menu choice")
        print("Bill to date: ${:.2f}".format(total_cost))
        print("Total Distance travelled: {}km".format(get_total_distance()))
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    print("You Travelled {}km".format(get_total_distance()))
    list_taxis()


def get_taxi_choice():
    print("Taxis available:")
    list_taxis()
    taxi_choice = get_valid_int_input("Choose taxi: ")

    while taxi_choice not in range(len(TAXIS)):
        print("Invalid taxi choice")
        taxi_choice = get_valid_int_input("Choose taxi: ")

    return TAXIS[taxi_choice]


def list_taxis():
    for (i, taxi) in enumerate(TAXIS):
        print("{} - {}".format(i, taxi))


def get_valid_int_input(prompt):
    valid_input = False
    user_input = None

    while not valid_input:
        try:
            user_input = int(input(prompt))
            valid_input = True
        except ValueError:
            print("Invalid input")

    return user_input


def drive_taxi(current_taxi):
    current_taxi.start_fare()
    drive_distance = get_valid_int_input("Drive how far? ")
    current_taxi.drive(drive_distance)
    print("Your {} trip will cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
    return current_taxi.get_fare()


def get_total_distance():
    return sum([taxi.odometer for taxi in TAXIS])


if __name__ == '__main__':
    main()
