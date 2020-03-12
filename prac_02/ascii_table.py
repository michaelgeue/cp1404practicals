ASCII_LOWER = 33
ASCII_UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = int(input("Enter a number between {} and {}: ".format(ASCII_LOWER, ASCII_UPPER)))
    while number < ASCII_LOWER or number > ASCII_UPPER:
        print("Invalid number")
        number = int(input("Enter a number between {} and {}: ".format(ASCII_LOWER, ASCII_UPPER)))
    print("The character for {} is {}".format(number, chr(number)))

    columns = int(input("How many columns would you like to print? "))
    for i in range(33, 128, columns):
        string = ""
        for number in range(columns):
            string = string + "{:3} {}  ".format(i + number, chr(i + number))
        print(string)


main()
