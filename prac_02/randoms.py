import random
print(random.randint(5, 20))  # Line 1
# A random number is shown. Smallest number being 5 and the largest being 20

print(random.randrange(3, 10, 2))  # Line 2
# A random number that goes up to but not including the end number. Smallest number is 3, largest is 10.
# Line 2 could not produce 4 as the range of potential numbers are incremented by 2.

print(random.uniform(2.5, 5.5))  # Line 3
# A randomly generated number to 16 decimal places. Smallest number generated is 2.5, largest is 5.5.

print(random.randint(1, 100))
