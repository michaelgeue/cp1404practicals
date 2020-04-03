def main():
    user_email = input("Email: ")
    email_dict = {}

    while not user_email == "":

        if "@" not in user_email:
            print("E-mail must contain @")
            user_email = input("Email: ")
        else:
            name = (user_email.split("@")[0]).split(".")
            name = " ".join(name).title()
            user_confirm = input("Is your name {}? (y/n) ".format(name)).lower()

            while user_confirm not in "yn":
                print("Invalid input")
                user_confirm = input("Is your name {}? (y/n) ".format(name)).lower()

            if user_confirm == "n":
                name = input("Name: ").title()

            email_dict[name] = email_dict.get(name, user_email)
            print(email_dict)
            user_email = input("Email: ")

    print("")

    for name, email in email_dict.items():
        print("{} ({})".format(name, email))


main()
