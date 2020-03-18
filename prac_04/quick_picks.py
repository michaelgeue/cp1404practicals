from random import choice
NUMBERS = [number for number in range(1, 46)]


def main():
    tickets = int(input("How many quick picks? "))
    for ticket in range(tickets):
        numbers = []
        while len(numbers) != 6:
            number = choice(NUMBERS)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        for number in numbers:
            print("{:2}".format(number), end=" ")
        print("")


main()
