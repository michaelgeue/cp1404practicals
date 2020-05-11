"""
Sort Files 1 Practical
"""

import os
import shutil


def main():
    os.chdir("FilesToSort")

    for filename in os.listdir("."):
        file_extension = filename[filename.find(".") + 1:]
        make_directory(file_extension)
        shutil.move(filename, file_extension)


def make_directory(file_extension):
    try:
        os.mkdir(file_extension)
    except FileExistsError:
        pass


main()
