MINIMUM_LENGTH = 4

password = input("Password: ({} characters minimum) ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    print("Invalid password")
    password = input("Password: ({} characters minimum) ".format(MINIMUM_LENGTH))

print("*" * len(password))
