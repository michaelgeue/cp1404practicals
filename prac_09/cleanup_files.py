"""
CP1404/CP5632 Practical
Cleanup Files Practical
"""

import os


def main():
    """"Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""

    for (i, char) in enumerate(filename):
        if i == 0 or filename[i - 1] == "(" or filename[i - 1] == "_":
            # Capitalises first letter of file, after opening bracket and after underscore
            new_name += char.upper()

        elif (char.isupper() or char == "(") and filename[i - 1] != "_" \
                or filename[i - 2: i] == "'s" and filename[i] != "_" \
                or filename[i - 4:i] == "your" and (filename[i] != "s" and filename[i] != "_"):
            # Adds space before Capital letter and brackets as well as after "'s" e.g:(It'syourblood.txt)
            # Adds space after word your if word does not continue or if space does not exist e.g:(It'syourblood.txt)
            new_name += "_{}".format(char.upper())

        elif filename[i - 3:i] == "You" and filename[i:i+2] == "ll":
            # Add apostrophe to word eg:(YoullCome.txt)
            new_name += "'{}".format(char)

        else:
            new_name += char

    print("{} renamed to {}".format(filename, new_name))
    return new_name


main()

