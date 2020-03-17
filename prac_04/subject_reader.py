"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = get_subject_data()
    for subject in subject_data:
        print("{:6} is taught by {:^12} and has {:3} students".format(subject[0], subject[1], subject[2]))


def get_subject_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open("subject_data.txt", 'r')
    subject_data = []

    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)

    input_file.close()
    return subject_data


main()
