def main():
    out_file = open("data.txt", 'w')
    print(input("Please enter your name: ").title(), file=out_file)
    out_file.close()

    in_file = open("data.txt", 'r')
    print("Your name is {}".format(in_file.read()))
    in_file.close()

    out_file = open("numbers.txt", 'w')
    print("17\n42\n400", file=out_file)
    out_file.close()

    in_file = open("numbers.txt", 'r')
    total = 0
    for i in range(2):
        total += int(in_file.readline())
    print(total)
    in_file.close()

    in_file = open("numbers.txt", 'r')
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
    in_file.close()


main()
