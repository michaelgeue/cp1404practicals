def main():

    numbers = [int(input("Number 1: "))]
    # Add numbers to list until user enters negative
    while not numbers[-1] < 0:
        numbers.append(int(input("Number {}: ".format(len(numbers) + 1))))

    del numbers[-1]

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average number is {}".format(sum(numbers) / len(numbers)))

    print("-" * 20)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    login = input("Username: ")
    if login in usernames:
        print("Access granted")
    else:
        print("Access denied")

    print("-" * 20)


main()
