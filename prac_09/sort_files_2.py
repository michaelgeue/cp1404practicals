"""
Sort Files 2 Practical
"""

import os
import shutil


def main():
    os.chdir("FilesToSort")
    extension_to_dir = {}

    for filename in os.listdir("."):
        file_extension = get_file_extension(filename)

        if file_extension not in extension_to_dir:
            extension_to_dir[file_extension] = get_user_input(file_extension)

        directory = extension_to_dir[file_extension]
        make_directory(directory)
        shutil.move(filename, directory)


def get_user_input(extension):
    return input("What category would you like to sort {} files into? ".format(extension))


def get_file_extension(filename):
    return filename[filename.find(".") + 1:]


def make_directory(file_extension):
    try:
        os.mkdir(file_extension)
    except FileExistsError:
        pass


main()
