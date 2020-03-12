from random import uniform


def main():
    out_file = open("temps_input.txt", 'w')
    out_file.close()

    for temps in range(0, 15):
        temperature = uniform(-200, 200)
        out_file = open("temps_input.txt", 'a')
        print(temperature, file=out_file)
        out_file.close()


main()
