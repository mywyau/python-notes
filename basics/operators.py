exponent = 2 ** 3
modulus = 22 % 8
division = 22 / 8
multiplication = 3 * 3
subtraction = 5 - 2
addition = 5 + 10


def main():
    listOfCalcs = [exponent, modulus, division, multiplication, subtraction, addition]
    listOfCalcNames = ["exponent", "modulus", "division", "multiplication", "subtraction", "addition"]
    zipped = zip(listOfCalcs, listOfCalcNames)
    print(list(zipped))


if __name__ == "__main__":
    main()
