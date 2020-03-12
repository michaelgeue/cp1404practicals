def main():
    print("Number sequence generator")
    start_number = int(input("Please enter starting range number "))
    end_number = int(input("Please enter end range number: "))

    while end_number == start_number or end_number < start_number:
        print("Sorry, end range number must be more than starting range number")
        end_number = int(input("Please enter end range number: "))

    print("\nEven numbers:\n")
    for i in range(start_number, end_number + 1):
        if i % 2 == 0:
            print(i, end=' ')

    print("\nOdd numbers:\n")
    for i in range(start_number, end_number + 1):
        if i % 2 == 1:
            print(i, end=' ')

    print("\nSquares:\n")
    for i in range(start_number, end_number +1):
        print(i * i, end=' ')


main()
