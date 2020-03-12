"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    from random import randint
    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))

    grade = grade_list(score)
    print(grade)

    score = randint(0, 100)
    print("\nRandom score: {}".format(score))
    grade = grade_list(score)
    print(grade)


def grade_list(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
