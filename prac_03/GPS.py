from random import uniform


def main():
    population = 1000
    year = 1
    print("Welcome to the Gopher Population Simulator!\nStarting population: {}\nYear 1".format(population))
    for year in range(2, 11):
        gophers_born = birth(population)
        gophers_died = death(population)
        population = population + gophers_born - gophers_died
        print("\n{} gophers were born. {} died.\nPopulation: {}\nYear {}""".format
              (gophers_born, gophers_died, population, year))


def birth(population):
    return int(round(population * uniform(0.1, 0.2)))


def death(population):
    return int(round(population * uniform(0.05, 0.25)))


main()
