HEX_COLOURS = {"aliceblue": "#f0f8ff", "beige": "#f5f5dc", "black": "#000000", "cadetblue": "#5f9ea0",
               "coral": "#ff7f50", "chocolate": "#d2691e", "forestgreen": "#228b22", "firebrick": "#b22222",
               "goldenrod": "#daa520", "light": "#eedd82"}


def main():
    print(HEX_COLOURS)

    colour_choice = input("Enter colour: ").lower()

    while colour_choice != "":
        if colour_choice in HEX_COLOURS:
            print("{} is {}".format(colour_choice, HEX_COLOURS[colour_choice]))
        else:
            print("Invalid colour")
        colour_choice = input("Enter colour: ").lower()


main()
