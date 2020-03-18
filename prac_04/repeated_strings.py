def main():
    strings = [input("Input string: ")]
    while not strings[-1] == "":
        strings.append(input("Input string: "))
    del strings[-1]

    repeated_strings = []
    for string in strings:
        if strings.count(string) > 1 and string not in repeated_strings:
            repeated_strings.append(string)

    if len(repeated_strings) == 0:
        print("No repeated strings entered")
    else:
        print("\nStrings repeated:")
        for string in repeated_strings:
            print(string)


main()
