value1 = True
value2 = False
value3 = bool(0)
value4 = bool(0.5)
value5 = bool(-0.5)
value6 = bool([])
value7 = bool([1, 2, 3, 4, 5, 6])
value8 = bool("")
value9 = bool("spam")

ids = ["True", "False", "bool(0)", "bool(0.5)", "bool(-0.5)""bool([])", "bool([1, 2, 3, 4, 5, 6])", "bool("")",
       "bool(\"spam\")"]

values = [value1, value2, value3, value4, value5, value6, value7, value8, value9]

namedValues = list(zip(ids, values))

trueValue1 = 1 == 1
falseValue1 = 1 != 2
trueValue2 = 5 > 0
falseValue2 = 20 < 0
trueValue3 = 10 >= 10
falseValue3 = 15 <= 10

operators = ["==", "!=", ">", "<", ">=", "<="]

values2 = [
    trueValue1,
    falseValue1,
    trueValue2,
    falseValue2,
    trueValue3,
    falseValue3,
]

relationalOperators = list(zip(operators, values2))


def main():
    [print(v) for v in namedValues]
    [print(v) for v in relationalOperators]


if __name__ == "__main__":
    main()
