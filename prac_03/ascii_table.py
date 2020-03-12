ASCII_LOWER = 33
ASCII_UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))

    number = get_number(ASCII_LOWER, ASCII_UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    columns = int(input("How many columns would you like to print? "))
    for i in range(ASCII_LOWER, ASCII_UPPER + 1, columns):
        string = ""
        for number in range(columns):
            string = string + "{:3} {}  ".format(i + number, chr(i + number))
        print(string)


def get_number(ascii_lower, ascii_upper):
    number = 0
    while number < ascii_lower or number > ascii_upper:
        try:
            number = int(input("Enter a number ({}-{}): ".format(ascii_lower, ascii_upper)))
            if number < ascii_lower or number > ascii_upper:
                print("Invalid number!")
        except ValueError:
            print('Invalid number!')
    return number


main()
