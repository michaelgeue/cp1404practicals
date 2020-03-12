def main():
    minimum_length = 4
    password = get_password(minimum_length)
    hide_password(password)


def get_password(minimum_length):
    password = input("Password: ({} characters minimum) ".format(minimum_length))
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Password: ({} characters minimum) ".format(minimum_length))
    return password


def hide_password(password):
    print("*" * len(password))

main()

