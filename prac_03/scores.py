from random import randint


def main():
    number_of_scores = 0
    while number_of_scores <= 0:
        try:
            number_of_scores = int(input("How many scores? "))
            if number_of_scores <= 0:
                print("Invalid number")
        except ValueError:
            print("Invalid number")

        out_file = open("results.txt", 'w')
        out_file.close()

        for score in range(0, number_of_scores):
            result = randint(0, 100)
            grade = grade_list(result)
            out_file = open("results.txt", 'a')
            print("{} is {}".format(result, grade), file=out_file)
            out_file.close()


def grade_list(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
