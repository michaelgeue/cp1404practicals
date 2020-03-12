def main():
    in_file = open("temps_input.txt", 'r')
    temp_list = in_file.readlines()
    in_file.close()
    out_file = open("temps_output.txt", 'w')
    out_file.close()
    for temperature in temp_list:
        celsius = fahrenheit_to_celsius(float(temperature))
        out_file = open("temps_output.txt", "a")
        print(celsius, file=out_file)
        out_file.close()


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()