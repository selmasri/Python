MONTHS_IN_YEAR = 12
def happy_birthday():
    name = input("Your name: ")
    month = input("Birth month: ")
    day = input("Birth day of the month: ")
    year = input("Birth year: ")

    print(name, ", your birthday is on",
        month, day, ",", year)

def main():
    happy_birthday()
    happy_birthday()
    happy_birthday()
    happy_birthday()

main()
