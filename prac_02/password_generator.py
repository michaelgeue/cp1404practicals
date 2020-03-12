def main():
    from random import choice
    print("Automatic Password Generator\n")

    lower_characters = "abcdefghijklmnopqrstuvwxyz"
    upper_characters = lower_characters.upper()
    numeric_characters = "0123456789"
    special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
    options_list = [("lower case", lower_characters), ("upper case", upper_characters), ("numeric", numeric_characters),
                    ("special", special_characters)]
    word_requirement_list = [lower_characters, upper_characters, numeric_characters, special_characters]

    for option in options_list:
        valid_input = False

        while not valid_input:
            char_requirement = input("Do you require {} characters (Y/N): ".format(option[0])).upper()
            if char_requirement == "Y":
                valid_input = True
            elif char_requirement == "N":
                word_requirement_list.remove(option[1])
                valid_input = True
            else:
                print("Invalid input")
                valid_input = False

    minimum_length = len(word_requirement_list)

    if minimum_length != 0:
        word_length = 0
        while word_length < minimum_length:
            try:
                word_length = int(input("How many letters (Minimum {} characters) ".format(minimum_length)))
                if word_length < minimum_length:
                    print("Invalid number")
            except ValueError:
                print("Invalid number")
    else:
        print("No password for you.")
        exit()

    password = ""

    while word_length != 0:
        char_type = choice(word_requirement_list)
        password += choice(char_type)
        if word_length == len(word_requirement_list):
            word_requirement_list.remove(char_type)
        word_length -= 1

    print("Your password is {}".format(password))


main()
