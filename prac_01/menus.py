def main():
    name = input("Enter name: ")
    user_input = input("(H)ello\n(G)oodbye\n(Q)uit\n").upper()
    while user_input != "Q":
        if user_input == "H":
            print("Hello", name)
        elif user_input == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")
        user_input = input("(H)ello\n(G)oodbye\n(Q)uit\n").upper()


main()
