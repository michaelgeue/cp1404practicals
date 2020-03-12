"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    valid_format = False
    word_format = ""

    while not valid_format:
        word_format = input("""Enter format for word "c" for consonants "v" for vowels): """).lower()
        valid_format = is_valid_format(word_format)

    word = ""

    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format(word_format):
    word_format_choices = "cv"
    for char in word_format:
        if char not in word_format_choices:
            print("Invalid format")
            return False
    return True


main()
