def main():
    numbers_one = [1, 2, 3, 7, 8, 9]
    numbers_two = [4, 5, 6]
    added_numbers = add_memberwise(numbers_one, numbers_two)
    print("Adding {} and {} together is {}".format(numbers_one, numbers_two, added_numbers))


def add_memberwise(numbers_one, numbers_two):
    numbers_in_list = [len(numbers_one), len(numbers_two)]
    numbers_to_leave = (numbers_in_list[0] - numbers_in_list[1])

    longest_list = []
    if numbers_to_leave > 0:
        longest_list = numbers_one
    elif numbers_to_leave < 0:
        longest_list = numbers_two

    numbers_to_leave = abs(numbers_to_leave)
    numbers_to_add = max(numbers_in_list) - numbers_to_leave
    added_numbers = []

    for number in range(numbers_to_add):
        added_numbers.append(numbers_one[number] + numbers_two[number])

    if not numbers_to_leave == 0:
        for number in range(numbers_to_leave):
            added_numbers.append(longest_list[numbers_to_add + number])

    return added_numbers


main()
