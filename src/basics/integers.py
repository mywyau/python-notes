oneHundered1 = int("100")
twoHundred = int("200")
positiveRoundInt = int(3.5)
negativeRoundInt = int(-3.5)


def printIntExamples():
    listOfInts = [oneHundered1, twoHundred, positiveRoundInt, negativeRoundInt]
    [print(x) for x in listOfInts]


def main():
    printIntExamples()


if __name__ == "__main__":
    main()
